""" definicja reguł dla wyszukiwania urzędów w SHG """
# cspell: disable


def rule_patterns_wicesoltysi() -> list:
    """ definicje reguł """
    patterns = [
        # wicesołtys
        [{"LEMMA":"wicesołtys"}],
        # wicesołtys + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"wicesołtys"}, {"POS":"ADJ", "OP": "+"}],
        # wicesołtys + przymiotnik i przymiotnik
        [{"LEMMA":"wicesołtys"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # wicesołtys + nazwa własna (lub parę nazw)
        [{"LEMMA":"wicesołtys"}, {"ENT_TYPE":"PLACENAME", "OP": "*"}],
        # wicesołtys + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"wicesołtys"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wicesołtys w nazwa (lub parę)
        [{"LEMMA":"wicesołtys"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wicesołtys z nazwa
        [{"LEMMA":"wicesołtys"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wicesołtys ze + nazwa
        [{"LEMMA":"wicesołtys"}, {"LOWER":"ze"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wicesołtys m. nazwa
        [{"LEMMA":"wicesołtys"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wicesołtys miasta nazwa
        [{"LEMMA":"wicesołtys"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wicesołtys wsi nazwa
        [{"LEMMA":"wicesołtys"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wicesołtys z wsi nazwa
        [{"LEMMA":"wicesołtys"}, {"LOWER":"z"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wicesołtys ze wsi nazwa
        [{"LEMMA":"wicesołtys"}, {"LOWER":"ze"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}]
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
        # wicesołtys + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # wicesołtys + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        # wicesołtys + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        # wicesołtys + 'm' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    # wicesołtys z + skrót miejscowości np.: A.
    for litera in litery:
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wicesołtys"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"},
                         {"IS_PUNCT":True}])

    patterns_output = []
    for item in patterns:
        patterns_output.append({"label": "OCCUPATION_MUNICIPAL",
                                "pattern": item,
                                "id": "wicesołtysi"})

    return patterns_output
