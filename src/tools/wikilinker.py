""" proste linkowanie encji z WikiHum """
# cspell: disable
from wikibaseintegrator import wbi_helpers
from wikibaseintegrator import WikibaseIntegrator
from wikibaseintegrator.wbi_config import config as wbi_config
from rapidfuzz import process


wbi_config['USER_AGENT'] = 'MyWikibaseBot/1.0'
wbi_config['MEDIAWIKI_API_URL'] = 'https://wikihum.lab.dariah.pl/api.php'
wbi_config['SPARQL_ENDPOINT_URL'] = 'https://wikihum.lab.dariah.pl/bigdata/sparql'
wbi_config['WIKIBASE_URL'] = 'https://wikihum.lab.dariah.pl'


def fuzzylinker_people(search_entity:str, df, year:str="") -> str:
    """ funkcja wyszukuje najbardziej prawdopodobną kndydaturę osoby z bazy
        na podstawe imienia i nazwiska oraz daty śmierci, z użyciem biblioteki rapidfuzz
    """
    best_qid = ''
    best_description = ''

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
                break
        elif death_date and not year:
            if int(death_date)>= 1000 and int(death_date) <= 1625:
                best_qid = qid
                best_description = description
                break

    return best_qid, best_description


def wikilinker_people(search_entity:str, year:str="", number_of_candidates=10, instance='Q5') -> str:
    """ funkcja wyszukuje w wikibase najlepiej pasujący identyfikator dla osoby
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


def fuzzylinker_places(search_entity:str, df) -> str:
    """ funkcja wyszukuje najbardziej prawdopodobną kandydaturę miejscowości z bazy
        na podstawe nazwy, z użyciem biblioteki rapidfuzz
    """
    best_qid = best_description = best_latitude = best_longitude = ''

    if len(search_entity) >= 3:
        result = process.extract(search_entity, df['Miejscowosc'], score_cutoff=90, limit=150)
        # obecnie pobiera pierwszą miejscowość z proponowanych
        for item in result:
            name, score, line_number = item
            best_qid = df['QID'][line_number]
            best_description = df['Description'][line_number]
            best_latitude = df['Latitude'][line_number]
            best_longitude = df['Longitude'][line_number]

            #wbi = WikibaseIntegrator()
            #place_item = wbi.item.get(entity_id=best_qid)
            #best_description = place_item.descriptions.get('pl')
            break

    return best_qid, best_description, best_latitude, best_longitude
