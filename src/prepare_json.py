""" results """
import json
import time
import re
from pathlib import Path


def get_text_with_year(text: str) -> str:
    """ zwraca początek tekstu z rokiem, latami"""
    result = ''
    znaki = '0123456789-— ,aAn.[]'
    for i in text:
        if i in znaki:
            result += i
        else:
            break

    return result.rstrip()


def get_year_from_regest(text) -> str:
    """zwraca rok lub lata z regestu """

    result = ""
    patterns = [
                r'\[\d{4}\]',
                r'\[\d{4}\s?-\s?\d{1,4}(,\s+\d{4}\s?-\s?\d{1,4})+\]',
                r'\[\d{4}\s?-\s?\d{1,2}\]',

                r'ok\.\s+\d{4}',
                r'^a\.\s+\d{4}\s?-\s?\d{1}(n\.){0,1}',
                r'^a\.\s+\d{4}(n\.){0,1}',
                r'^A\.\s+\d{4}(,\s+\d{4}(n\.){0,1})*',
                r'^\d{4}(n\.){0,1}'
                r'\d{4}-przed\s+\d{4}',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){2})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){3})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){4})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){5})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){6})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){7})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){8})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){9})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){10})*',
                r'\d{4}((,\s+\d{4}(n\.){0,1}){11})*',
                r'\d{4}\s?-\s?\d{2},\s+\d{4},\s+\d{4},\s+\d{4},\s+\d{4}\s?-\s?\d{1},\s+\d{4},\s+\d{4}\s?-\s?\d{1}(n\.){0,1}',
                r'\d{4},\s+\d{4},\s+\d{4}-\d{1},\s+\d{4}-\d{1}(,\s+\d{4}(n\.){0,1})*',
                r'\d{4}(,\s+[\d-]{4,7}(n\.){0,1})*',
                r'\d{4},\s+\d{4}-\d{1},\s+\d{4},\s+\d{4}-\d{1}(n\.){0,1}',
                r'\d{4}-\d{2},\s+\d{4}-\d{1}(,\s+\d{4}(n\.){0,1})*',
                r'\(\d{4}\s?-\s?\d{1}\)\s+\d{4}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{2},\s+\d{4},\s+\d{4}(n\.){0,1}',
                r'\d{4}(n\.){1},\s+\d{4}-\d{2}(n\.){1}',
                r'\d{4}\/\d{1},\s+\d{4},\s+\d{4}',
                r'\d{4},\s+\d{4},\s+\d{4}',
                r'\d{4}-\d{2},\s+\d{4}-\d{1},\s+\d{4}-\d{1},\s+\d{4}-\d{1},\s+\d{4}-\d{1}',
                r'\d{4}-\d{1},\s+\d{4}-\d{1},\s+\d{4}-\d{1}',
                r'\d{4},\s+\d{4}\s?-\s?\d{2},\s+\d{4},\s+\d{4}(n\.){0,1}',
                r'\d{4},\s+\d{4}\s?-\s?\d{2},\s+\d{4},\s+\d{4},\s+\d{4}(n\.){0,1}',
                r'\d{4},\s+\d{4}\s?-\s?\d{2}(n\.){0,1}',
                r'\d{4},\s+\d{4},\s+\d{4}-\d{2}(n\.){0,1}',
                r'\d{4},\s+\d{4}\s?-\s?\d{1}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{1},\s+\d{4}\s?-\s?\d{1}(n\.){0,1}',
                r'\d{4},\s+\d{4},\s+\d{4}-\d{1}(,\s+\d{4}(n\.){0,1})*',
                r'\d{4}-\d{2},\s+\d{4}-\d{4},\s+\d{4}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{2},\s+\d{4}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{1},\s+\d{4}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{2},\s+\d{4}\s?-\s?\d{4}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{2},\s+\d{4}\s?-\s?\d{1}(n\.){0,1}',
                r'\d{4},\s*\d{4}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{4}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{2}(n\.){0,1}',
                r'\d{4}\s?-\s?\d{1}(n\.){0,1}',
                r'\d{4}\d{4}(n\.){0,1}',
                r'\d{4}-\d{3}(n\.){0,1}'
               ]

    for pattern in patterns:
        begin_text = get_text_with_year(text)
        match = re.search(pattern, begin_text)
        temp = ""
        if match:
            temp = match.group()
        if len(temp) > len(result):
            result = temp.strip()

    return result


def xsplit(s:str):
    """ funkcja dzieli przekazany tekst na wiersze według średnika pomijając
        jednak średniki w nawiasach, zwraca listę
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

def prepare_regest(value: str) -> tuple():
    """ przetwarzanie regestu """
    pos = value.rfind("(")
    # jeżeli regest z bibliografią
    if pos != -1:
        value_content = value[:pos]
        value_source = str(value[pos:])
        value_date = get_text_with_year(value_content)
        value_content = value_content[len(value_date):]
    # jeżeli regest bez bibliografii
    else:
        value_content = value
        value_source = ""
        value_date = get_text_with_year(value_content)
        value_content = value_content[len(value_date):]

    value_date = value_date.strip()
    value_source = value_source.strip()
    value_content = value_content.strip()
    value_source_bg = value_source_en = ''
    value_source_list = []

    if value_source.startswith('('):
        value_source_bg = '('
        value_source = value_source[1:]
        pos_en = value_source.rfind(')')
        value_source_en = value_source[pos_en:]
        value_source = value_source[:pos_en]
        value_source_list.append({"source_bg": value_source_bg})

    if ';' in value_source:
        tmp = value_source.split(';')
    else:
        tmp = [value_source]

    for element_tmp in tmp:
        value_source_list.append({"source_el": element_tmp.strip()})

    if value_source_en:
        value_source_list.append({"source_en":value_source_en.strip()})

    return value_date, value_content, value_source_list


if __name__ == '__main__':

    # pomiar czasu wykonania
    start_time = time.time()

    # poprawione wyniki dla functions
    data_folder = Path("..") / "json_krak_cz_V_z_1"
    filename = '30659_old.json'
    path = Path("..") / "json_krak_cz_V_z_1" / filename
    output_path = Path("..") / "json_krak_cz_V_z_1" / filename.replace("_old.json","_new.json")

    type_count = {}
    with open(path, "r", encoding='utf-8') as f:
        json_data = json.load(f)
        item_text = json_data["text"]

        # regesty
        for point in item_text:
            point_num = point["point_num"]
            point_content = point["point_content"]
            lista_content = []
            for point_item in point_content:
                if "regesty" in point_item:
                    regesty = point_item["regesty"]
                    del point_item['regesty']
                    lista = xsplit(regesty)
                    for item in lista:
                        # jeżeli zastosowano nietypowy podział regestów np. zwykłą
                        # kropką i znakiem \n zamiast ;
                        if '\n' in item:
                            tmp_list = item.split('\n')
                            for tmp_list_item in tmp_list:
                                item_date, item_content, source_list = prepare_regest(tmp_list_item)
                                lista_content.append({"regest":{"date":item_date,
                                                                "content":item_content,
                                                                "source": source_list}})
                        else:
                            item_date, item_content, source_list = prepare_regest(item)
                            lista_content.append({"regest":{"date":item_date,
                                                            "content":item_content,
                                                            "source": source_list}})
                else:
                    lista_content.append(point_item)

            del point["point_content"]
            point["point_content"] = lista_content

        with open(output_path, 'w', encoding='utf-8') as f_out:
            json.dump(json_data, f_out, indent=4, ensure_ascii=False)

    # czas wykonania programu
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Czas wykonania programu: {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))} s.')
