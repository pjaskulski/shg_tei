""" definicja reguł dla wyszukiwania urzędów w SHG """
# cSpell:disable


def rule_patterns_przysiezni() -> list:
    """ definicje reguł """
    patterns = [
        # przysięgły, przysiężny
        [{"LEMMA":{"IN": ["przysięgły", "przysiężny"]}}],
        # przysiężny, przysięgły z/w + nazwa
        [{"LEMMA":{"IN": ["przysiężny", "przysięgły"]}},
         {"LOWER":{"IN": ["w", "z", "ze"]}}, {"ENT_TYPE":"PLACENAME"}],
    ]

    # w zeszycie 1 z części V SHG występują tylko miejscowości na M i N
    # litery = 'ABCDEFGHIJKLMNOPRSTUWZŚŻŹĆŁ'
    litery = 'MN'
    for litera in litery:
        patterns.append([{"LEMMA":{"IN":["przysiężny", "przysięgły"]}},
                         {"LOWER":{"IN":["w", "z", "ze"]}}, {"TEXT":f"{litera}"},
                         {"IS_PUNCT": True}])

    return patterns
