""" proste linkowanie encji z WikiHum """
# cspell: disable
from wikibaseintegrator import wbi_helpers
from wikibaseintegrator import WikibaseIntegrator
from wikibaseintegrator.wbi_config import config as wbi_config


wbi_config['USER_AGENT'] = 'MyWikibaseBot/1.0'
wbi_config['MEDIAWIKI_API_URL'] = 'https://wikihum.lab.dariah.pl/api.php'
wbi_config['SPARQL_ENDPOINT_URL'] = 'https://wikihum.lab.dariah.pl/bigdata/sparql'
wbi_config['WIKIBASE_URL'] = 'https://wikihum.lab.dariah.pl'


def wikilinker_people(search_entity:str, year:str="", number_of_candidates=10, instance='Q5') -> str:
    """ funkcja wyszukuje w wikibase najlepiej pasujący identyfikator dla osoby """
    wbi = WikibaseIntegrator()
    lista_qid = wbi_helpers.search_entities(search_entity, language='pl', search_type='item', max_results=number_of_candidates, allow_anonymous=True)

    if year and year.isdigit():
        year = int(year)
    else:
        year = 0

    best_qid = ''
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
                if instance_of_value == instance and year:
                    for item_date_death in list_date_death:
                        #print(item_date_death.mainsnak.datavalue)
                        if 'value' in item_date_death.mainsnak.datavalue:
                            date_death_value = item_date_death.mainsnak.datavalue['value']['time']
                            if len(date_death_value) > 5:
                                tmp_year = date_death_value[1:5]
                                if tmp_year.isdigit():
                                    year_of_death = int(tmp_year)
                                    if year_of_death >= year and year_of_death - year < 45:
                                        best_qid = item_qid
                                        print(best_qid)
                                        break

    return best_qid
