""" dodatkowe narzędzia """
# cspell: disable

def fstr(template, item_name:str, item_auth:str, autorzy:dict, profile_desc:str):
    """ f string dla zmiennej z zawartością z pliku txt """
    return eval(f'f"""{template}"""', locals())


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
