""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns_przysiezni() -> list:
    """ definicje reguł """
    patterns = [
        # przysięgły
        [{"LEMMA":"przysięgły"}],
        # przysiężny w + nazwa
        [{"LEMMA":"przysiężny"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME"}],
        # przysiężny z + nazwa
        [{"LEMMA":"przysiężny"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME"}],
    ]

    return patterns
