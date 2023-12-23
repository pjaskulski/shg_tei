""" json to TEI converter """
import json
import time
#import xml.dom.minidom
from pathlib import Path
import warnings
import spacy
import stanza
import spacy_stanza
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


warnings.filterwarnings("ignore")
stanza.download('pl')

MAKE_NER = True
NER_TYPE = 'stanza'

nlp = spacy_stanza.load_pipeline("pl", use_gpu=False)

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

# Skrót bieżącej miejscowości
skrot = 'M'

# translacja tagów z modelu na TEI
label2tag = {
                "geogName":"geogName",
                "persName":"persName",
                "placeName":"placeName",
                "orgName": "orgName",
                "date": "date",
                "PLACENAME":"placeName",
                "OCCUPATION": "roleName",
                "OBJECT": "objectName",
                "COATOFARMS": "heraldry",
                "ROLE1": "roleName",
                "ROLE2": "roleName",
                "PERSON": "persName",
                "OCCUPATION_CHURCH_LOW": "roleName",
                "OCCUPATION_CHURCH_HIGH": "roleName",
                "OCCUPATION_MUNICIPAL": "roleName",
                "OCCUPATION_LAND": "roleName"
}

# reguły ogólne i kościelne
pattern = patterns_ogolne(skrot=skrot, obiekty=obiekty, fizjografia=fizjografia)

# uzupełnienia reguł dla urzędów
# reguły dla burmistrzów
patterns_burmistrzowie = rule_patterns_burmistrzowie()
for item in patterns_burmistrzowie:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "burmistrz"})

# reguły dla podwojtow
patterns_podwojtowie = rule_patterns_podwojtowie()
for item in patterns_podwojtowie:
    pattern.append({"label": "OCCUPATION_MUNICIPAL",
                    "pattern": item,
                    "id": "podwójt"})

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

# wzorce encji
wzorce_encji.add_patterns(pattern)

# słownik autorów (rozwijanie skrótów)
autorzy = {"JL":"Jacek Laberschek"}
item_foot = None


################################### FUNKCJE ####################################
def fstr(template):
    """ f string dla zmiennej z zawartością z pliku txt """
    return eval(f'f"""{template}"""')


def add_footnotes(value:str, max:int) -> str:
    """ funkcja zmienia tagi przypisów na docelowe """
    for i in range(1, max + 1):
        value = value.replace(f'[[{i}]]', f'<note n="{i}" type="footnote">{item_foot[str(i)]}</note>')
    return value


def ner_to_xml(value:str) -> str:
    """ wyszukiwanie encji - nazw własnych """
    # w trybie bez NER zwraca po prostu wartość wejściową
    if not MAKE_NER:
        return value

    # Process the text
    doc = nlp(value)

    # Iterate over the entities and tag person entities
    tagged_text = ""
    last_index = 0
    for ent in doc.ents:
        if (ent.label_ in label2tag) and (ent.label_ != "ORGNAME" or len(ent.text) > 3) :
            if ent.label_ == "OBJECT":
                tagged_text += (value[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="obj[{ent.lemma_}]">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "FIZJOGRAFIA":
                tagged_text += (value[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="fiz[{ent.lemma_}]">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "OCCUPATION_CHURCH_LOW":
                tagged_text += (value[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="kościelny_niższy" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "OCCUPATION_CHURCH_HIGH":
                tagged_text += (value[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="kościelny_wyższy" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "OCCUPATION_MUNICIPAL":
                tagged_text += (value[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="miejski" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            elif ent.label_ == "OCCUPATION_LAND":
                tagged_text += (value[last_index:ent.start_char] +
                                f'<{label2tag[ent.label_]} type="ziemski" subtype="{ent.ent_id_}">{ent.text}</{label2tag[ent.label_]}>')
            else:
                tagged_text += (value[last_index:ent.start_char] +
                                f"<{label2tag[ent.label_]}>{ent.text}</{label2tag[ent.label_]}>")
            last_index = ent.end_char
    tagged_text += value[last_index:]

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

    # poprawione wyniki dla functions
    data_folder = Path("..") / "json_krak_cz_V_z_1"
    filename = '30659.json'
    path = Path("..") / "json_krak_cz_V_z_1" / filename

    type_count = {}
    with open(path, "r", encoding='utf-8') as f:
        json_data = json.load(f)
        item_type = json_data["type"]
        item_id = json_data["type"]
        item_dict = json_data["dictionary"]
        item_name = json_data["name"]
        item_text = json_data["text"]
        item_auth = json_data["author"]
        item_foot = json_data["footnotes"]
        num_of_footnotes = len(item_foot)

        tei_header = fstr(header)

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
                        content = ner_to_xml(item["regest"]["content"])
                        content = add_footnotes(content, num_of_footnotes)
                        tei_text += f'{content}' + ' '
                    if 'source' in item['regest']:
                        biblio = item['regest']['source']
                        if biblio:
                            for bib_item in biblio:
                                if 'source_bg' in bib_item:
                                    tei_text += f'{bib_item["source_bg"]}'
                                elif 'source_el' in bib_item:
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
                # lista elementów
                elif "elements" in item:
                    tei_text += '<p>\n'
                    for el in item["elements"]:
                        el = ner_to_xml(el)
                        el = add_footnotes(el, num_of_footnotes)
                        tei_text += f'<seg>{el}</seg>'
                    tei_text += '</p>\n'
                elif "paragraphs" in item:
                    for par in item["paragraphs"]:
                        par = ner_to_xml(par)
                        par = add_footnotes(par, num_of_footnotes)
                        tei_text += f'<p>{par}</p>\n'
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

        tei_text = tei_header + tei_text + '</body></text></TEI>'

        name_ner = ''
        if MAKE_NER:
            name_ner = '_' + NER_TYPE

        output_path2 = Path("..") / "tei" / filename.replace('.json',name_ner + '.xml')

        with open(output_path2, "w", encoding='utf-8') as f_out_1:
            f_out_1.write(tei_text)

    # czas wykonania programu
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Czas wykonania programu: {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))} s.')
