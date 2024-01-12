""" json to TEI converter for SHG (historical geographical dictionary) entries"""
# cspell: disable
import os
import json
import time
import re
#import xml.dom.minidom
from pathlib import Path
import warnings
import spacy
import pandas as pd
import roman
from patterns.burmistrzowie import rule_patterns_burmistrzowie
from patterns.podwojtowie import rule_patterns_podwojtowie
from patterns.sedziowie import rule_patterns_sedziowie
from patterns.pisarze import rule_patterns_pisarze
from patterns.notariusze import rule_patterns_notariusze
from patterns.ogolne import patterns_ogolne
from patterns.lawnicy import rule_patterns_lawnicy
from patterns.rajcowie import rule_patterns_rajcowie
from patterns.soltysi import rule_patterns_soltysi
from patterns.wojtowie import rule_patterns_wojtowie
from patterns.landwojtowie import rule_patterns_landwojtowie
from patterns.przysiezni import rule_patterns_przysiezni
from patterns.wicesoltysi import rule_patterns_wicesoltysi
from patterns.monety import rule_patterns_coin
# from tools.wikilinker import wikilinker_people
from tools.wikilinker import fuzzylinker_people, fuzzylinker_places


warnings.filterwarnings("ignore")

MAKE_NER = True

nlp = spacy.load('pl_nask')
spacy.require_cpu()

config = {
   "overwrite_ents": True
}
wzorce_encji = nlp.add_pipe("entity_ruler", config=config)

# wczytanie słowników obiektów i fizjografii
path_obiekty = Path("..") / "slowniki" / "obiekty.csv"
with open(path_obiekty, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    obiekty = [x.strip() for x in lines]

path_fizjografia = Path("..") / "slowniki" / "fizjografia.csv"
with open(path_fizjografia, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    fizjografia = [x.strip() for x in lines]

# wczytanie słowników staropolskich imion i miejscowości
path_imiona = Path("..") / "slowniki" / "imiona.csv"
with open(path_imiona, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    imiona = [x.strip() for x in lines]

path_miejscowosci = Path("..") / "slowniki" / "miejscowosci.csv"
with open(path_miejscowosci, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    miejscowosci = [x.strip() for x in lines]

# wczytanie form podstawowych dla miejscowości
places_norm = {}
path_mianowniki = Path("..") / "slowniki" / "places_norm.csv"
with open(path_mianowniki, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        tmp = line.split(',')
        places_norm[tmp[0].strip()] = tmp[1].strip()

# translacja tagów z modelu na TEI
label2tag = {
            "GEOGNAME":"geogName",
            "PERSNAME":"persName",
            "PLACENAME":"placeName",
            "ORGNAME": "orgName",
            "DATE": "date",
            "OCCUPATION": "roleName",
            "OBJECT": "objectName",
            "FIZJOGRAFIA": "objectName",
            "COATOFARMS": "heraldry",
            "PERSON": "persName",
            "OCCUPATION_CHURCH_LOW": "roleName",
            "OCCUPATION_CHURCH_HIGH": "roleName",
            "OCCUPATION_MUNICIPAL": "roleName",
            "OCCUPATION_LAND": "roleName",
            "COIN": "unit"
        }

# reguły (entity ruler), ogólne: obiekty gospodarcze, fizjograficzne, urzędy kościelne,
# urzędy ziemskie, reguły dla urzędów miejskich burmistrzów, wójtów itp.
pattern = (
            patterns_ogolne(obiekty=obiekty, fizjografia=fizjografia,
                          imiona=imiona, miejscowosci=miejscowosci)
            + rule_patterns_burmistrzowie()
            + rule_patterns_podwojtowie()
            + rule_patterns_sedziowie()
            + rule_patterns_pisarze()
            + rule_patterns_notariusze()
            + rule_patterns_lawnicy()
            + rule_patterns_rajcowie()
            + rule_patterns_soltysi()
            + rule_patterns_wojtowie()
            + rule_patterns_landwojtowie()
            + rule_patterns_przysiezni()
            + rule_patterns_wicesoltysi()
            + rule_patterns_coin()
        )

#print(len(pattern))
# wzorce encji
wzorce_encji.add_patterns(pattern)

# słownik autorów (rozwijanie skrótów)
autorzy = {"JL":"Jacek Laberschek",
           "FS": "Franciszek Sikora",
           "JS": "Janusz Szyszka",
           "KN": "Karol Nabiałek",
           "WB": "Waldemar Bukowski",
           "MS": "Michał Schmidt",
           "ZK": "Zuzanna Kulpa",
           "MW": "Michał Wojenka",
           "Zuzanna Kulpa": "Zuzanna Kulpa",
           "None": ""
          }

person_shortcuts = {"jag.":"Jagiellończyk",
                    "Jag.":"Jagiellończyk",
                    "wstydl.": "Wstydliwy",
                    "Wstydl.": "Wstydliwy",
                    "mik.": "Mikołaj",
                    "Mik.": "Mikołaj",
                    "Stan.": "Stanisław",
                    "stan.": "Stanisław",
                    "Olbr.": "Olbracht",
                    "olbr.": "Olbracht",}

# baza osób z WikiHum
people_path = Path('..') / 'slowniki' / 'people.csv'
df_people = pd.read_csv(people_path, sep=',', header=0, low_memory=False,
                        quotechar='"', encoding='utf-8')
df_people['DateOfDeath'] = df_people['DateOfDeath'].fillna(0)
df_people['DateOfDeath'] = df_people['DateOfDeath'].astype(int)

# baza miejscowości z WikiHum (istniejące w 16 wieku w woj krakowskim i przyległych powiatach)
places_path = Path('..') / 'slowniki' / 'places.csv'
df_places = pd.read_csv(places_path, sep=',', header=0, low_memory=False,
                        quotechar='"', encoding='utf-8')

# miasta w 16 wieku w całej bazie WikiHum
miasta_path = Path("..") / "slowniki" / "miasta_1600.csv"
df_miasta = pd.read_csv(miasta_path, sep=',', header=0, low_memory=False,
                        quotechar='"', encoding='utf-8')

# miejscowości współczesne z południowo wschodniej Polski
south_east_path = Path("..") / "slowniki" / "south_east_poland.csv"
df_south_east = pd.read_csv(south_east_path, sep=',', header=0, low_memory=False,
                        quotechar='"', encoding='utf-8')

item_foot = None
main_place_latitude = main_place_longitude = None

people = {}
places = {}

################################### FUNKCJE ####################################
def fstr(template):
    """ f string dla zmiennej z zawartością z pliku txt """
    return eval(f'f"""{template}"""')


def add_footnotes(text_to_complete:str, max_footnotes:int) -> str:
    """ funkcja zmienia tagi przypisów na docelowe """
    # jeżeli są jakieś przypisy
    if max_footnotes:
        for i in range(1, max_footnotes + 1):
            text_to_complete = text_to_complete.replace(f'[[{i}]]', f'<note n="{i}" type="footnote">{item_foot[str(i)]}</note>')

    return text_to_complete


def ner_to_xml(text_to_process:str, r_date:str="", main_place:str="") -> str:
    """ wyszukiwanie encji - nazw własnych """
    # w trybie bez NER zwraca po prostu wartość wejściową
    if not MAKE_NER:
        return text_to_process

    #print(value)

    # Process the text
    doc = nlp(text_to_process)

    # Iterate over the entities and tag person entities
    tagged_text = ""
    last_index = 0
    for ent in doc.ents:
        if (ent.label_ in label2tag) and (ent.label_ != "ORGNAME" or len(ent.text) > 3) :
            if ent.label_ == "OBJECT":
                if ent.lemma_ == 'kol.':
                    ent_lemma_value = 'kolegiata'
                elif ent.lemma_ == 'kat.':
                    ent_lemma_value = 'katedra'
                elif ent.lemma_ == 'kl.':
                    ent_lemma_value = 'klasztor'
                elif ent.lemma_ == 'folw.':
                    ent_lemma_value = 'folwark'
                else:
                    ent_lemma_value = ent.lemma_
                tagged_text += (text_to_process[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="obj" subtype="{ent_lemma_value}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "FIZJOGRAFIA":
                if ent.lemma_ == 'jez.':
                    ent_lemma_value = 'jezioro'
                elif ent.lemma_ == 'rz.':
                    ent_lemma_value = 'rzeka'
                else:
                    ent_lemma_value = ent.lemma_
                tagged_text += (text_to_process[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="fiz" subtype="{ent_lemma_value}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "OCCUPATION_CHURCH_LOW":
                tagged_text += (text_to_process[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="kościelny_niższy" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "OCCUPATION_CHURCH_HIGH":
                tagged_text += (text_to_process[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="kościelny_wyższy" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "OCCUPATION_MUNICIPAL":
                tagged_text += (text_to_process[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="miejski" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "OCCUPATION_LAND":
                tagged_text += (text_to_process[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="ziemski" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "COIN":
                tagged_text += (text_to_process[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="currency" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "DATE":
                tmp_date = str(ent.text)
                if tmp_date.isdigit() and len(tmp_date) == 4:
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f'<{label2tag[ent.label_]} when="{tmp_date}">{ent.text}</{label2tag[ent.label_]}>')
                elif not tmp_date.endswith('—') and ('-' in tmp_date or '—' in tmp_date):
                    sep = '-'
                    if '—' in tmp_date:
                        sep = '—'
                    tmp_date_tab = tmp_date.split(sep)
                    if len(tmp_date_tab[1]) < 4:
                        tmp_date_tab[1] = tmp_date_tab[0][:(4-len(tmp_date_tab[1]))] + tmp_date_tab[1]
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f'<{label2tag[ent.label_]} from="{tmp_date_tab[0]}" to="{tmp_date_tab[1]}">{ent.text}</{label2tag[ent.label_]}> ')
                elif ' ' in tmp_date and not '[' in tmp_date and not 'po' in tmp_date and not 'przed' in tmp_date:
                    pattern = r'\d{1,2}\s+[XVI]+\s+\d{4}'
                    match = re.search(pattern=pattern, string=tmp_date)
                    if match:
                        match_text = match.group()
                        match_tab = match_text.split(' ')
                        day = match_tab[0]
                        month = str(roman.fromRoman(match_tab[1].strip()))
                        year = match_tab[2]
                        tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f'<{label2tag[ent.label_]} when="{year}-{month.zfill(2)}-{day.zfill(2)}">{ent.text}</{label2tag[ent.label_]}>')
                    else:
                        pattern = r'\d{4}'
                        match = re.search(pattern=pattern, string=tmp_date)
                        if match:
                            year = match.group()
                            tagged_text += (text_to_process[last_index:ent.start_char] +
                                        f'<{label2tag[ent.label_]} when="{year}">{ent.text}</{label2tag[ent.label_]}>')
                        else:
                            tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f"<{label2tag[ent.label_]}>{ent.text}</{label2tag[ent.label_]}>")
                else:
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f"<{label2tag[ent.label_]}>{ent.text}</{label2tag[ent.label_]}>")
            elif ent.label_ == 'PERSNAME' or ent.label_ == 'PERSON':
                qid = ''
                # tylko dla osób z nazwiskiem, wieloma imionami lub miejscowością z której się piszą
                if ' ' in ent.text:
                    text_to_search = ent.lemma_
                    text_to_search = text_to_search.replace('[','').replace(']','')
                    text_to_search = text_to_search.title()
                    if " Z " in text_to_search:
                        text_to_search = text_to_search.replace(" Z ", " z ")

                    for short, long in person_shortcuts.items():
                        if short in text_to_search:
                            text_to_search = text_to_search.replace(short, long)

                    # qid, description = wikilinker_people(search_entity=text_to_search, year=r_date)
                    qid, description, alias = fuzzylinker_people(search_entity=text_to_search, df=df_people, year=r_date)

                    #print(ent.text, '->', text_to_search, '->', qid)

                if qid:
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f'<{label2tag[ent.label_]} ref="#{qid}">{ent.text}</{label2tag[ent.label_]}>')
                    people[text_to_search] = (qid, description, alias)
                else:
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f"<{label2tag[ent.label_]}>{ent.text}</{label2tag[ent.label_]}>")
            elif ent.label_ == 'PLACENAME':
                text_to_search = ent.lemma_
                # sprawdzenie czy występuje w słowniku mianowników dla trudniejszych
                # nazw miejscowości
                if ent.text in places_norm:
                    text_to_search = places_norm[ent.text]
                alt_text = ent.text

                # jeżeli nazwa to skrót od miejscowości hasła to szukanie wg nazwy miejscowości hasła
                # czyli zamiast M. - Mstów
                if (len(text_to_search) == 2 and
                    text_to_search.endswith('.') and
                    text_to_search[0].lower() == main_place[0].lower()):
                    text_to_search = main_place
                    text_to_search = text_to_search.title()

                # jeżeli nazwa zaczyna się z małej litery (np. z powodu lematyzacji) to poprawka
                if text_to_search[0].islower():
                    text_to_search = text_to_search.title()

                qid, description, latitude, longitude, qid_label = fuzzylinker_places(search_entity=text_to_search,
                                                                           alt_search_entity=alt_text,
                                                                           m_place_latitude=main_place_latitude,
                                                                           m_place_longitude=main_place_longitude,
                                                                           df=df_places,
                                                                           alt_df=df_miasta,
                                                                           modern_df=df_south_east)
                if qid:
                    #print(ent.text, '->', text_to_search, '->', qid)
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f'<{label2tag[ent.label_]} ref="#{qid}">{ent.text}</{label2tag[ent.label_]}>')
                    # uzupełnienie do spisu miejscowości
                    places[qid_label] = (qid, description, latitude, longitude)
                    print(f"{text_to_search} ({alt_text}) = {qid_label} ({qid}) - {description}")
                else:
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                f"<{label2tag[ent.label_]}>{ent.text}</{label2tag[ent.label_]}>")
            else:
                tagged_text += (text_to_process[last_index:ent.start_char] +
                                f"<{label2tag[ent.label_]}>{ent.text}</{label2tag[ent.label_]}>")
            last_index = ent.end_char
    tagged_text += text_to_process[last_index:]

    return tagged_text


def xsplit(s:str):
    """ funkcja dzieli przekazany tekst na wiersze według średnika pomijając
        jednak średniki w nawiasach zwykłych i kwadratowych, zwraca listę
    """
    parts = []
    bracket_level = 0
    bracket_level_2 = 0
    current = []
    # trick to remove special-case of trailing chars
    for c in (s + ";"):
        if c == ";" and bracket_level == 0 and bracket_level_2 == 0:
            parts.append("".join(current))
            current = []
        else:
            if c == "(":
                bracket_level += 1
            elif c == ")":
                bracket_level -= 1
            elif c == "[":
                bracket_level_2 += 1
            elif c == "]":
                bracket_level_2 -= 1

            current.append(c)
    return parts


#################################### MAIN ######################################
if __name__ == '__main__':

    # pomiar czasu wykonania
    start_time = time.time()

    # header template
    path_header = Path("..") / "templates" / "header.txt"
    with open(path_header, 'r', encoding='utf-8') as f_h:
        header = f_h.read()

    # źródłowe pliki json do konwersji na pliki TEI XML
    data_folder = Path("..") / "json"
    data_folder_list = data_folder.glob('*.json')

    # folder na pliki wyjściowe TEI XML
    output_folder = Path("..") / "tei"

    for data_file in data_folder_list:
        filename = os.path.basename(data_file)

        # jeżeli tylko wybrany plik
        # if filename != "30659.json":
        #    continue

        output_path = Path("..") / "tei" / filename.replace('.json', '.xml')
        if os.path.exists(output_path):
            print(f"Plik {filename.replace('.json','.xml')} już istnieje")
            continue

        print(f"Przetwarzanie: {filename}")

        path = Path("..") / "json" / filename

        type_count = {}
        with open(path, "r", encoding='utf-8') as f:
            json_data = json.load(f)
            item_type = json_data["type"]
            item_id = json_data["type"]
            item_dict = json_data["dictionary"]
            item_name = json_data["name"]
            item_text = json_data["text"]
            item_auth = item_foot = None
            num_of_footnotes = 0
            if "author" in json_data:
                item_auth = json_data["author"]
            if "footnotes" in json_data:
                item_foot = json_data["footnotes"]
                num_of_footnotes = len(item_foot)

            if not item_auth:
                item_auth = "None"

            # identyfikacja głównej miejscowości hasła, ustalenie jej współrzędne
            text_to_search = item_name.title()
            _, _, main_place_latitude, main_place_longitude, _ = fuzzylinker_places(text_to_search, '', None, None, df_places)
            #print(f"Współrzędne miejscowości {text_to_search}: {main_place_latitude}, {main_place_longitude}")

            # head
            tei_text = f"""<text>
                <body>
                    <head>{item_name}</head>
            """
            # punkty
            for point in item_text:
                point_num = point["point_num"]
                point_content = point["point_content"]
                tei_text += f'\n<div type="point" n="{point_num}">\n'
                previous_item = ''
                # regesty i teksty
                for item in point_content:
                    # akapit tekstowy
                    if 'text' in item:
                        if previous_item == 'regest':
                            tei_text += '\n</p>\n'
                        if '\n' in item["text"]:
                            tmp = item["text"].split('\n')
                        else:
                            tmp = [item["text"]]
                        for tmp_item in tmp:
                            content = ner_to_xml(tmp_item, main_place=item_name)
                            content = add_footnotes(content, num_of_footnotes)
                            tei_text += f'\n<p>\n{content}\n</p>\n'
                            previous_item = 'text'
                    # lista regestów
                    elif 'regest' in item:
                        regest_date = ""
                        if previous_item != 'regest':
                            tei_text += '\n<p>\n'
                            previous_date = ""
                        tei_text += '\n<seg>'
                        if 'date' in item['regest'] and item["regest"]["date"].strip() != "":
                            regest_date = item["regest"]["date"]

                            # jeżeli data dzienna YYYY DD MM
                            pattern = r'\d{4}\s+\d{1,2}\s+[XVI]+'
                            match = re.search(pattern=pattern, string=regest_date)
                            # czy może data dzienna w formie DD MM YYYY
                            pattern2 = r'\d{1,2}\s+[XVI]+\s+\d{4}'
                            match2 = re.search(pattern=pattern2, string=regest_date)

                            # YYYY DD MM
                            if match:
                                tmp_data = match.group().strip()
                                tmp_data_tab = tmp_data.split(' ')
                                year = tmp_data_tab[0].strip()
                                day = tmp_data_tab[1].strip()
                                month = str(roman.fromRoman(tmp_data_tab[2].strip()))
                                tei_text += f'<date when="{year}-{month.zfill(2)}-{day.zfill(2)}">{regest_date}</date>' + ' '
                                #previous_date = f'[<date>{regest_date}</date>]' + ' '
                                previous_date = f'<date when="{year}-{month.zfill(2)}-{day.zfill(2)}"/> '
                            # DD MM YYYY
                            elif match2:
                                tmp_data = match.group().strip()
                                tmp_data_tab = tmp_data.split(' ')
                                year = tmp_data_tab[2].strip()
                                day = tmp_data_tab[0].strip()
                                month = str(roman.fromRoman(tmp_data_tab[1].strip()))
                                tei_text += f'<date when="{year}-{month.zfill(2)}-{day.zfill(2)}">{regest_date}</date>' + ' '
                                #previous_date = f'[<date>{regest_date}</date>]' + ' '
                                previous_date = f'<date when="{year}-{month.zfill(2)}-{day.zfill(2)}"/> '

                            # jeżeli nietypowy zapis daty wówczas z atrybutem when-custom w tagu <date>
                            elif regest_date and ('[' in regest_date or 'po' in regest_date):
                                tei_text += f'<date>{regest_date}</date>' + ' '
                                #previous_date = f'[<date>{regest_date}</date>]' + ' '
                                previous_date = f'<date when-custom="{regest_date}"/> '

                            # bardziej typowy zapis daty z atrybutami w tagu <date>
                            elif regest_date and regest_date.strip() != '':
                                if ',' in regest_date:
                                    tmp = regest_date.split(',')
                                    tmp = [x.strip() for x in tmp]
                                    tmp_tab = []
                                    tmp_prev_tab = []
                                    for tmp_date_item in tmp:
                                        if '-' in tmp_date_item:
                                            tmp = tmp_date_item.split('-')
                                            if len(tmp[1]) < 4:
                                                tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                            tmp_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}">{tmp_date_item}</date> ')
                                            tmp_prev_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"/> ')
                                        elif '—' in tmp_date_item:
                                            tmp = tmp_date_item.split('—')
                                            if len(tmp[1]) < 4:
                                                tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                            tmp_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"> {tmp_date_item}</date> ')
                                            tmp_prev_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"/> ')
                                        elif r'/' in tmp_date_item:
                                            tmp = tmp_date_item.split(r'/')
                                            if len(tmp[1]) < 4:
                                                tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                            tmp_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"> {tmp_date_item}</date> ')
                                            tmp_prev_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"/> ')
                                        else:
                                            tmp_tab.append(f'<date when="{tmp_date_item.strip()}">{tmp_date_item}</date>')
                                            tmp_prev_tab.append(f'<date when="{tmp_date_item.strip()}"/>')
                                    tei_text += ', '.join(tmp_tab)
                                    previous_date = ', '.join(tmp_prev_tab)

                                # zakres dat
                                elif '-' in regest_date:
                                    tmp = regest_date.split('-')
                                    if len(tmp[1]) < 4:
                                        tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                    tei_text += f'<date from="{tmp[0]}" to="{tmp[1]}">{regest_date}</date> '
                                    #previous_date = f'[<date from="{tmp[0]}" to="{tmp[1]}">{regest_date}</date>] '
                                    previous_date = f'<date from="{tmp[0]}" to="{tmp[1]}"/> '

                                # inny format zakresu dat
                                elif '—' in regest_date:
                                    tmp = regest_date.split('—')
                                    if len(tmp[1]) < 4:
                                        tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                    tei_text += f'<date from="{tmp[0]}" to="{tmp[1]}"> {regest_date}</date> '
                                    #previous_date = f'[<date from="{tmp[0]}" to="{tmp[1]}"> {regest_date}</date>] '
                                    previous_date = f'<date from="{tmp[0]}" to="{tmp[1]}"/> '

                                # przełom lat
                                elif r'/' in regest_date:
                                    tmp = regest_date.split(r'/')
                                    if len(tmp[1]) < 4:
                                        tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                    tmp_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"> {regest_date}</date> ')
                                    #previous_date = f'<date from="{tmp[0]}" to="{tmp[1]}"> {regest_date}</date> '
                                    previous_date = f'<date from="{tmp[0]}" to="{tmp[1]}"/> '
                                else:
                                    tei_text += f'<date when="{item["regest"]["date"]}">{item["regest"]["date"]}</date>' + ' '
                                    #previous_date = f'[<date when="{item["regest"]["date"]}">{item["regest"]["date"]}</date>]' + ' '
                                    previous_date = f'<date when="{item["regest"]["date"]}"/>'
                        # jeżeli nie ma dat a poprzednio był regest z datą to obowiązuje ta sama data
                        else:
                            if previous_date:
                                tei_text += previous_date

                        if 'content' in item['regest']:
                            content = ner_to_xml(item["regest"]["content"], r_date=regest_date, main_place=item_name)
                            content = add_footnotes(content, num_of_footnotes)
                            tei_text += f'{content}' + ' '
                        if 'source' in item['regest']:
                            biblio = item['regest']['source']
                            if biblio:
                                for bib_item in biblio:
                                    if 'source_bg' in bib_item:
                                        tei_text += f'{bib_item["source_bg"]}'
                                    elif 'source_el' in bib_item and bib_item["source_el"].strip() != "":
                                        source_el = bib_item["source_el"]
                                        if 's.' in source_el:
                                            pos = source_el.find('s.')
                                            source_el_format = f'<title>{source_el[:pos]}</title> '
                                            source_el_format += f'<biblScope>{source_el[pos:]}</biblScope>'
                                        elif 't.' in source_el:
                                            pos = source_el.find('t.')
                                            source_el_format = f'<title>{source_el[:pos]}</title> '
                                            source_el_format += f'<biblScope>{source_el[pos:]}</biblScope>'
                                        elif 'z.' in source_el:
                                            pos = source_el.find('z.')
                                            source_el_format = f'<title>{source_el[:pos]}</title> '
                                            source_el_format += f'<biblScope>{source_el[pos:]}</biblScope>'
                                        elif ',' in source_el:
                                            tmp = source_el.split(',')
                                            source_el_format = f'<title>{tmp[0]}</title>'
                                            for element in tmp[1:]:
                                                source_el_format += ', ' + f'<biblScope>{element}</biblScope>'

                                        else:
                                            source_el_format = f'<title>{source_el}</title>'

                                        # sklejanie bibliografii
                                        if tei_text.endswith('('):
                                            tei_text += f'<bibl>{source_el_format}</bibl>'
                                        else:
                                            tei_text += f'; <bibl>{source_el_format}</bibl>'

                                    elif 'source_en' in bib_item:
                                        tmp = add_footnotes(bib_item["source_en"], num_of_footnotes)
                                        tei_text += f'{tmp}'
                        if tei_text.endswith(';') or tei_text.endswith('.'):
                            tei_text += '</seg>'
                        else:
                            tei_text += ';</seg>'

                        previous_item = 'regest'
                    # lista elementów przetwarzana na sekcje <seg>
                    elif "elements" in item:
                        tmp_list = item["elements"]
                        for el in tmp_list:
                            el = ner_to_xml(el, main_place=item_name)
                            el = add_footnotes(el, num_of_footnotes)
                            tei_text += f'<seg>{el}</seg>'
                        tei_text += '</p>\n'
                    # lista elementów przetwarzana na sekcje <p>
                    elif "paragraphs" in item:
                        for par in item["paragraphs"]:
                            par = ner_to_xml(par, main_place=item_name)
                            par = add_footnotes(par, num_of_footnotes)
                            tei_text += f'<p>{par}</p>\n'
                    # akapit z ppozycjami bibliograficznymi oddzielonymi znakiem
                    # średnika, przetwarzany na sekcje <bibl>
                    elif "bibliography" in item:
                        tei_text += '<p>\n'
                        bibl_text = item['bibliography']
                        tmp = xsplit(bibl_text)
                        tmp = [f'<bibl>{x.strip()}</bibl>' for x in tmp]
                        #for bibl_item in tmp:
                        #    tei_text += f'<bibl>{bibl_item}</bibl>'
                        tei_text += '; '.join(tmp)
                        tei_text += '</p>\n'

                if previous_item == 'regest':
                    tei_text += '\n</p>\n'

                tei_text += '</div>\n'

            # autor
            if item_auth and item_auth != "None":
                tei_text += f"""<div>
                <p><bibl><author sameAs="{autorzy[item_auth]}">{item_auth}</author></bibl></p>
                </div>
                """

            if item_foot:
                tei_text += '\n<div>\n<p>\n'
                for key, value in item_foot.items():
                    value_ner = ner_to_xml(value, main_place=item_name)
                    tei_text += f'<seg type="footnote" n="{key}">{key}. {value_ner}</seg>\n'
                tei_text += '\n</p>\n</div>\n'

            # lista rozpoznanych w wiki osób
            profile_desc = ""
            people_printed = []
            if len(people) > 0:
                profile_desc += "<profileDesc>\n<particDesc>\n<listPerson>\n"
                for key, value in people.items():
                    value_qid, value_desc, value_alias = value
                    if value_qid not in people_printed:
                        profile_desc += f'''<person xml:id="{value_qid}">
                        <persName>{value_alias}</persName>
                        <idno>https://wikihum.lab.dariah.pl/wiki/Item:{value_qid}</idno>
                        <note>{value_desc}</note>
                        </person>
                        '''
                        people_printed.append(value_qid)
                profile_desc += "</listPerson>\n</particDesc>\n"

            # lista rozpoznanych w wiki miejscowości
            if len(places) > 0:
                print(f"places: {len(places)}")
                if not profile_desc:
                    profile_desc += "<profileDesc>\n"

                profile_desc += "<settingDesc>\n<listPlace>\n"
                for key, value in places.items():
                    value_qid, value_desc, value_lat, value_lon = value
                    profile_desc += f'''<place xml:id="{value_qid}">
                    <placeName>{key}</placeName>
                    <location>
                    <geo>{value_lat}, {value_lon}</geo>
                    </location>
                    <idno>https://wikihum.lab.dariah.pl/wiki/Item:{value_qid}</idno>
                    <note>{value_desc}</note>
                    </place>
                    '''

                profile_desc += "</listPlace>\n</settingDesc>\n"

            if profile_desc:
                profile_desc += "</profileDesc>\n"

            # nagłówek
            tei_header = fstr(header)

            tei_text = tei_header + tei_text + '</body></text></TEI>'

            output_path2 = Path("..") / "tei" / filename.replace('.json','.xml')
            with open(output_path2, "w", encoding='utf-8') as f_out_1:
                f_out_1.write(tei_text)

    # czas wykonania programu
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Czas wykonania programu: {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))} s.')
