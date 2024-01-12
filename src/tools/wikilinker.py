""" proste linkowanie encji z WikiHum """
# cspell: disable
from wikibaseintegrator import wbi_helpers
from wikibaseintegrator import WikibaseIntegrator
from wikibaseintegrator.wbi_config import config as wbi_config
from rapidfuzz import process
import geopy.distance
import math


wbi_config['USER_AGENT'] = 'MyWikibaseBot/1.0'
wbi_config['MEDIAWIKI_API_URL'] = 'https://wikihum.lab.dariah.pl/api.php'
wbi_config['SPARQL_ENDPOINT_URL'] = 'https://wikihum.lab.dariah.pl/bigdata/sparql'
wbi_config['WIKIBASE_URL'] = 'https://wikihum.lab.dariah.pl'


def fuzzylinker_people(search_entity:str, df, year:str="") -> tuple:
    """ funkcja wyszukuje najbardziej prawdopodobną kndydaturę osoby z bazy
        na podstawe imienia i nazwiska oraz daty śmierci, z użyciem biblioteki rapidfuzz
    """
    best_qid = ''
    best_description = ''
    best_alias = ''

    if year and year.isdigit():
        year = int(year)
    else:
        year = 0

    result = process.extract(search_entity, df['Alias'], score_cutoff=90, limit=150)
    for item in result:
        name, score, line_number = item
        qid = df['QID'][line_number]
        description = df['Description'][line_number]

        alias = df['Alias'][line_number]
        # pomijane pojedyncze imiona, w 99% to powoduje fałszywe dopasowania
        if not ' ' in alias:
            continue

        death_date = df['DateOfDeath'][line_number]

        if death_date and year:
            if (int(death_date) >= int(year)) and (int(death_date) - int(year) < 45):
                best_qid = qid
                best_description = description
                best_alias = alias
                break
        elif death_date and not year:
            if int(death_date)>= 1000 and int(death_date) <= 1625:
                best_qid = qid
                best_description = description
                best_alias = alias
                break

    return best_qid, best_description, best_alias


def wikilinker_people(search_entity:str, year:str="", number_of_candidates=10, instance='Q5') -> str:
    """ funkcja wyszukuje bezpośrednio w wikibase najlepiej pasujący identyfikator dla osoby
        z kontrolą daty śmierci osoby w zakresie sensownym dla SHG
    """
    wbi = WikibaseIntegrator()
    lista_qid = wbi_helpers.search_entities(search_entity, language='pl', search_type='item', max_results=number_of_candidates, allow_anonymous=True)

    if year and year.isdigit():
        year = int(year)
    else:
        year = 0

    best_qid = ''
    best_description = ''
    for item_qid in lista_qid:
        my_item = wbi.item.get(entity_id=item_qid)
        claims = my_item.claims.claims
        if 'P27' not in claims:
            continue
        if 'P12' not in claims:
            continue

        list_instance_of = claims.get('P27')
        list_date_death = claims.get('P12')

        for item_instance_of in list_instance_of:
            if 'value' in item_instance_of.mainsnak.datavalue:
                instance_of_value = item_instance_of.mainsnak.datavalue['value']['id']
                if instance_of_value == instance:
                    if year:
                        for item_date_death in list_date_death:
                            if 'value' not in item_date_death.mainsnak.datavalue:
                                continue
                            date_death_value = item_date_death.mainsnak.datavalue['value']['time']
                            if len(date_death_value) > 5:
                                tmp_year = date_death_value[1:5]
                                if tmp_year.isdigit():
                                    year_of_death = int(tmp_year)
                                    if year_of_death >= year and year_of_death - year < 45:
                                        best_qid = item_qid
                                        best_description = my_item.descriptions.get(language='pl')
                                        # print(best_qid)
                                        break
                    else:
                        for item_date_death in list_date_death:
                            if 'value' not in item_date_death.mainsnak.datavalue:
                                continue
                            date_death_value = item_date_death.mainsnak.datavalue['value']['time']
                            if len(date_death_value) > 5:
                                tmp_year = date_death_value[1:5]
                                if tmp_year.isdigit():
                                    year_of_death = int(tmp_year)
                                    if year_of_death >= 1000 and year_of_death <= 1625:
                                        best_qid = item_qid
                                        best_description = my_item.descriptions.get(language='pl')

    return best_qid, best_description


def fuzzylinker_places(search_entity:str, alt_search_entity:str, m_place_latitude,
                       m_place_longitude, df, alt_df=None, modern_df=None) -> tuple:
    """ funkcja wyszukuje najbardziej prawdopodobną kandydaturę miejscowości z bazy
        na podstawie nazwy, z użyciem biblioteki rapidfuzz
        zwraca QID, opis z WikiHUM, współrzędne i etykietę
    """

    best_qid = best_description = best_latitude = best_longitude = best_label = ''

    # lista słów zwykle omyłkowo uznawanych za miejscowości dla których nie ma sensu szukać
    words = ["Polska", "Śląsk", "Węgry", "Czechy"]
    if search_entity in words:
        return best_qid, best_description, best_latitude, best_longitude, best_label

    # jeżeli alt_search_entity czyli oryginalna forma nazwy zaczyna się od małej litery
    # to nie jest to raczej miejscowość, lecz przymiotnik lub skrót i nie ma sensu identyfikować
    # w WikiHum
    if alt_search_entity and alt_search_entity[0].islower():
        return best_qid, best_description, best_latitude, best_longitude, best_label

    dataset = df
    # długość szukanej nazwy to minimum trzy znaki
    if len(search_entity) >= 3:
        result = process.extract(search_entity, df['Miejscowosc'], score_cutoff=90, limit=10)
        if len(result) == 0 and alt_search_entity:
            # szukanie alternatywne według nazwy w formie oryginalnie występującej
            # w tekście (lematyzacja czasem psuje nazwę)
            result = process.extract(alt_search_entity, df['Miejscowosc'], score_cutoff=90, limit=10)
            if len(result) == 0:
                # dla wielowyrazowych nazw próba szukania z odwróceniem kolejności wyrazów
                if ' ' in alt_search_entity:
                    tmp = alt_search_entity.split(' ')
                    new_alt_search_entity = tmp[1] + ' ' + tmp[0]
                    result = process.extract(new_alt_search_entity, df['Miejscowosc'], score_cutoff=90, limit=10)

        # jeżeli brak wyników szukanie w bazie miast z całej WikiHum (cała Polska)
        if len(result) == 0:
            print("Szukanie w bazie miast z XVI wieku...")
            result = process.extract(search_entity, alt_df['Miejscowosc'], score_cutoff=90, limit=10)
            dataset = alt_df

        # jeżeli brak wyników to szukanie w bazie miejscowości współczesnych z południowo -
        # wschodnej Polski (woj. śląskie, małopolskie, świętokrzyskie, podkarpackie)
        if len(result) == 0:
            print("Szukanie w bazie miejscowości współczesnych...")
            result = process.extract(search_entity, modern_df['Miejscowosc'], score_cutoff=90, limit=10)
            dataset = modern_df

        if len(result) == 0:
            print(f"Nie znaleziono kandydatów dla: {search_entity}")
        else:
            # wybór najlepszej miejscowości z proponowanych
            best_items = []
            best_score = 0
            best_item = None

            for item in result:
                name, score, line_number = item
                if score == 100:
                    best_items.append(item)
                else:
                    if score > best_score:
                        best_item = item
                        best_score = score

            if len(best_items) > 0:
                # jeżeli jest więcej niż jedna miejscowość z takim score i znane są
                # współrzędne głównej miejscowości hasła, szukana jest najbliższa
                if len(best_items) > 1 and m_place_latitude and m_place_longitude:
                    # if search_entity == 'Zawada':
                    #     print("Wybór z kandydatów:", best_items)
                    coords_main = (float(m_place_longitude), float(m_place_latitude))
                    best_distance = 999 # km
                    best_item = None
                    for item in best_items:
                        name, score, line_number = item
                        item_latitude = dataset['Latitude'][line_number]
                        item_longitude = dataset['Longitude'][line_number]
                        if not math.isnan(item_latitude) and not math.isnan(item_longitude):
                            coords_item = (float(item_longitude), float(item_latitude))
                            distance = geopy.distance.geodesic(coords_main, coords_item).km
                            if distance < best_distance:
                                best_item = item
                                best_distance = distance

                    name, score, line_number = best_item
                # jeżeli tylko jedna kandydatura miała score = 100
                else:
                    name, score, line_number = best_items[0]

            elif best_score > 0:
                name, score, line_number = best_item

            #print(name, score, line_number)
            best_qid = dataset['QID'][line_number]
            best_description = dataset['Description'][line_number]
            best_latitude = dataset['Latitude'][line_number]
            best_longitude = dataset['Longitude'][line_number]
            best_label = dataset["Miejscowosc"][line_number]

    return best_qid, best_description, best_latitude, best_longitude, best_label
