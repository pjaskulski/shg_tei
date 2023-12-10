""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns_soltysi() -> list:
    """ definicje reguł """
    patterns = [
        # sołtys + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"sołtys"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"POS":"ADJ", "OP": "+"}],
        # sołtys + przymiotnik i przymiotnik
        [{"LEMMA":"sołtys"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"sołtyska"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # sołtys + nazwa własna (lub parę nazw)
        [{"LEMMA":"sołtys"}, {"ENT_TYPE":"PLACENAME", "OP": "*"}],
        [{"LEMMA":"sołtyska"}, {"ENT_TYPE":"PLACENAME", "OP": "*"}],
        # sołtys + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"sołtys"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sołtys w nazwa (lub parę)
        [{"LEMMA":"sołtys"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sołtys z nazwa
        [{"LEMMA":"sołtys"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sołtys wsi nazwa
        [{"LEMMA":"sołtys"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sołtys z wsi nazwa
        [{"LEMMA":"sołtys"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sołtys ze wsi nazwa
        [{"LEMMA":"sołtys"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}]
    ]

    shortcuts = ["krak", "lel", "biec", "chęc", "czchow", "czech", "czes", "frank", "gnieźn",
                    "imbr", "jędrz", "kal", "Klar", "koprz", "ksiąs", "lub", "łęcz", "magd", "maz",
                    "miech", "miej", "mog", "mstow", "niem", "opocz", "ośw", "pilzn", "pol", "poł",
                    "pozn", "pras", "prosz", "przem", "rad", "roz", "san", "sand", "sądec",
                    "sieciech", "sier", "siew", "staniąt", "starosądec", "szczyrz", "śl", "średz",
                    "świętokrz", "świętop", "tyn", "wąch", "węg", "wiel", "wiśl", "wojn", "zator",
                    "zawich", "zwierzyn", "żarn", "żyd"]

    litery = 'ABCDEFGHIJKLMNOPRSTUWZŚŻŹĆŁ'

    for shortcut in shortcuts:
        # sołtys + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sołtys"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"sołtyska"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sołtys + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sołtys"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"sołtyska"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sołtys + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sołtys"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"sołtyska"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    # sołtys z + skrót miejscowości np.: A.
    for litera in litery:
        patterns.append([{"LEMMA":"sołtys"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"sołtyska"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
