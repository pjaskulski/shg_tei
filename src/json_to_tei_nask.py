""" json to TEI converter for SHG (historical geographical dictionary) entries"""
# cspell: disable
import os
import json
import time
#import xml.dom.minidom
from pathlib import Path
import warnings
import spacy
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
from tools.wikilinker import wikilinker_people


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

# reguły (entity ruler)
pattern = (
            # reguły ogólne: obiekty gospodarcze, fizjograficzne, urzędy kościelne, urzędy ziemskie
            patterns_ogolne(obiekty=obiekty, fizjografia=fizjografia,
                          imiona=imiona, miejscowosci=miejscowosci)
            # reguły dla burmistrzów
            + rule_patterns_burmistrzowie()
            # reguły dla podwojtow
            + rule_patterns_podwojtowie()
        )

# reguły dla sędziów
patterns_sedziowie = rule_patterns_sedziowie()
for item in patterns_sedziowie:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "sędzia"})

# reguły dla pisarzy
patterns_pisarze = rule_patterns_pisarze()
for item in patterns_pisarze:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "pisarz"})

# reguły dla notariuszy
patterns_notariusze = rule_patterns_notariusze()
for item in patterns_notariusze:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "notariusz"})

# reguły dla ławników
patterns_lawnicy = rule_patterns_lawnicy()
for item in patterns_lawnicy:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "ławnik"})

# reguły dla rajców
patterns_rajcowie = rule_patterns_rajcowie()
for item in patterns_rajcowie:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "rajca"})

# reguły dla sołtysów
patterns_soltysi = rule_patterns_soltysi()
for item in patterns_soltysi:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "sołtys"})

# reguły dla wójtów
patterns_wojtowie = rule_patterns_wojtowie()
for item in patterns_wojtowie:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "wójt"})

# reguły dla landwójtów
patterns_landwojtowie = rule_patterns_landwojtowie()
for item in patterns_landwojtowie:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "landwójt"})

# reguły dla przysiężnych
patterns_przysiezni = rule_patterns_przysiezni()
for item in patterns_przysiezni:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "przysiężny"})

# reguły dla wicesołtysów
patterns_wicesoltysi = rule_patterns_wicesoltysi()
for item in patterns_wicesoltysi:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "wicesołtysi"})

# reguły dla monet
patterns_coin = rule_patterns_coin()
for item in patterns_coin:
    pattern.append(item)

print(len(pattern))
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

item_foot = None

people = {}

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


def ner_to_xml(text_to_process:str, r_date:str="") -> str:
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
                else:
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f"<{label2tag[ent.label_]}>{ent.text}</{label2tag[ent.label_]}>")
            elif ent.label_ == 'PERSNAME':
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

                    qid, description = wikilinker_people(search_entity=text_to_search, year=r_date)
                    print(ent.text, '->', text_to_search, '->', qid)

                if qid:
                    tagged_text += (text_to_process[last_index:ent.start_char] +
                                    f'<{label2tag[ent.label_]} ref="#{qid}">{ent.text}</{label2tag[ent.label_]}>')
                    people[text_to_search] = (qid, description)
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
                            tei_text += '</p>'
                        if '\n' in item["text"]:
                            tmp = item["text"].split('\n')
                        else:
                            tmp = [item["text"]]
                        for tmp_item in tmp:
                            content = ner_to_xml(tmp_item)
                            content = add_footnotes(content, num_of_footnotes)
                            tei_text += f'<p>{content}</p>'
                            previous_item = 'text'
                    # lista regestów
                    elif 'regest' in item:
                        regest_date = ""
                        if previous_item != 'regest':
                            tei_text += '\n<p>'
                        tei_text += '\n<seg>'
                        if 'date' in item['regest']:
                            regest_date = item["regest"]["date"]
                            # jeżeli nietypowy zapis daty - bez atrybutów w tagu <date>
                            if regest_date and ('[' in regest_date or 'po' in regest_date):
                                tei_text += f'<date>{regest_date}</date>' + ' '
                            # bardziej typowy zapis daty z atrybutami w tagu <date>
                            elif regest_date and regest_date.strip() != '':
                                if ',' in regest_date:
                                    tmp = regest_date.split(',')
                                    tmp = [x.strip() for x in tmp]
                                    tmp_tab = []
                                    for tmp_date_item in tmp:
                                        if '-' in tmp_date_item:
                                            tmp = tmp_date_item.split('-')
                                            if len(tmp[1]) < 4:
                                                tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                            tmp_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}">{tmp_date_item}</date> ')
                                        elif '—' in tmp_date_item:
                                            tmp = tmp_date_item.split('—')
                                            if len(tmp[1]) < 4:
                                                tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                            tmp_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"> {tmp_date_item}</date> ')
                                        elif r'/' in tmp_date_item:
                                            tmp = tmp_date_item.split(r'/')
                                            if len(tmp[1]) < 4:
                                                tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                            tmp_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"> {tmp_date_item}</date> ')
                                        else:
                                            tmp_tab.append(f'<date when="{tmp_date_item.strip()}">{tmp_date_item}</date>')
                                    tei_text += ', '.join(tmp_tab)
                                elif '-' in regest_date:
                                    tmp = regest_date.split('-')
                                    if len(tmp[1]) < 4:
                                        tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                    tei_text += f'<date from="{tmp[0]}" to="{tmp[1]}">{regest_date}</date> '
                                elif '—' in regest_date:
                                    tmp = regest_date.split('—')
                                    if len(tmp[1]) < 4:
                                        tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                    tei_text += f'<date from="{tmp[0]}" to="{tmp[1]}"> {regest_date}</date> '
                                elif r'/' in regest_date:
                                    tmp = regest_date.split(r'/')
                                    if len(tmp[1]) < 4:
                                        tmp[1] = tmp[0][:(4-len(tmp[1]))] + tmp[1]
                                    tmp_tab.append(f'<date from="{tmp[0]}" to="{tmp[1]}"> {regest_date}</date> ')
                                else:
                                    tei_text += f'<date when="{item["regest"]["date"]}">{item["regest"]["date"]}</date>' + ' '
                        if 'content' in item['regest']:
                            content = ner_to_xml(item["regest"]["content"], r_date=regest_date)
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
                            el = ner_to_xml(el)
                            el = add_footnotes(el, num_of_footnotes)
                            tei_text += f'<seg>{el}</seg>'
                        tei_text += '</p>\n'
                    # lista elementów przetwarzana na sekcje <p>
                    elif "paragraphs" in item:
                        for par in item["paragraphs"]:
                            par = ner_to_xml(par)
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
                    value_ner = ner_to_xml(value)
                    tei_text += f'<seg type="footnote" n="{key}">{key}. {value_ner}</seg>\n'
                tei_text += '\n</p>\n</div>\n'

            # lista rozpoznanych w wiki osób
            profile_desc = ""
            if len(people) > 0:
                profile_desc += "<profileDesc>\n<particDesc>\n<listPerson>\n"
                for key, value in people.items():
                    value_qid, value_desc = value
                    profile_desc += f'''<person xml:id="{value_qid}">
                    <persName>{key}</persName>
                    <idno>https://wikihum.lab.dariah.pl/wiki/Item:{value_qid}</idno>
                    <note>{value_desc}</note>
                    </person>
                    '''
                profile_desc += "</listPerson>\n</particDesc>\n</profileDesc>\n"
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
