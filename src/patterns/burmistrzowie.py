""" definicje reguł dla wyszukiwania urzędów w SHG """
# cspell: disable


def rule_patterns_burmistrzowie() -> list:
    """ definicje reguł """
    patterns = [
        # burmistrz
        [{"LEMMA":"burmistrz"}],
        # burmistrz + nazwa
        [{"LEMMA":"burmistrz"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # burmistrz + przymiotnik
        [{"LEMMA":"burmistrz"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"burm."}, {"IS_PUNCT":True}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"POS":"ADJ", "OP": "+"}],
        # burmistrz miasteczka + nazwa
        [{"LEMMA":"burmistrz"}, {"LEMMA":"miasteczko"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LEMMA":"miasteczko"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LEMMA":"miasteczko"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # burmistrz miasta + nazwa
        [{"LEMMA":"burmistrz"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LEMMA":"miasto"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # burmistrz z +nazwa
        [{"LEMMA":"burmistrz"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # burmistrz w +nazwa
        [{"LEMMA":"burmistrz"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # burmistrz m. +nazwa
        [{"LEMMA":"burmistrz"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # burm. + nazwa
        [{"LEMMA":"burm"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # burmistrz miasta + nazwa
        [{"LEMMA":"burmistrz"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LEMMA":"miasto"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # burmistrz
        [{"LEMMA":"burmistrz"}]
    ]

    shortcuts = ["krak", "lel", "biec", "chęc", "czchow", "czech", "czes", "frank", "gnieźn",
                    "imbr", "jędrz", "kal", "Klar", "koprz", "ksiąs", "lub", "łęcz", "magd", "maz",
                    "miech", "miej", "mog", "mstow", "niem", "opocz", "ośw", "pilzn", "pol", "poł",
                    "pozn", "pras", "prosz", "przem", "rad", "roz", "san", "sand", "sądec",
                    "sieciech", "sier", "siew", "staniąt", "starosądec", "szczyrz", "śl", "średz",
                    "świętokrz", "świętop", "tyn", "wąch", "węg", "wiel", "wiśl", "wojn", "zator",
                    "zawich", "zwierzyn", "żarn", "żyd"]

    # w zeszycie 1 z części V SHG występują tylko miejscowości na M i N
    # litery = 'ABCDEFGHIJKLMNOPRSTUWZŚŻŹĆŁ'
    litery = 'MN'

    for shortcut in shortcuts:
        # burmistrz + skrót geogr.
        patterns.append([{"LEMMA":"burmistrz"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # burm. + skrót geogr.
        patterns.append([{"LOWER":"burm"}, {"IS_PUNCT":True},  {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])

        # burmistrz z + skrót miejscowości np.: burmistrz z A., burmistrz A.
        for litera in litery:
            patterns.append([{"LEMMA":"burmistrz"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                             {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrz"}, {"LOWER":"w"}, {"TEXT":f"{litera}"},
                             {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrz"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"z"},
                             {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"w"},
                             {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"burm"}, {"IS_PUNCT":True}, {"TEXT":f"{litera}"},
                             {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrzowie"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                             {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrzowie"}, {"LOWER":"w"}, {"TEXT":f"{litera}"},
                             {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrzowie"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    patterns_output = []
    for item in patterns:
        patterns_output.append({"label": "OCCUPATION_MUNICIPAL",
                        "pattern": item,
                        "id": "burmistrz"})

    return patterns_output
