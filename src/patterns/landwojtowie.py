""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns_landwojtowie() -> list:
    """ definicje reguł """
    patterns = [
        # landwójt
        [{"LEMMA":"landwójt"}],
        # landwójt + przymiotnik (lub parę przymiotników)
        [{"LOWER":"landwójt"}, {"POS":"ADJ", "OP": "+"}],
        # landwójt + przymiotnik i przymiotnik
        [{"LEMMA":"landwójt"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # landwójt + nazwa własna (lub parę nazw)
        [{"LEMMA":"landwójt"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"landwójt"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt + rzeczownik
        [{"LEMMA":"landwójt"}, {"POS":"NOUN", "OP": "+"}],
        # landwójt w nazwa (lub parę)
        [{"LEMMA":"landwójt"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt z nazwa
        [{"LEMMA":"landwójt"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt ze + nazwa
        [{"LEMMA":"landwójt"}, {"LOWER":"ze"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt m. nazwa
        [{"LEMMA":"landwójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt miasta nazwa
        [{"LEMMA":"landwójt"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt wsi nazwa
        [{"LEMMA":"landwójt"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt z wsi nazwa
        [{"LEMMA":"landwójt"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt ze wsi nazwa
        [{"LEMMA":"landwójt"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # landwójt sądu pr. niem. + nazwa
        [{"LEMMA":"landwójt"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"ENT_TYPE":"PLACENAME"}],
        # landwójt sądu prawa niem. + nazwa
        [{"LEMMA":"landwójt"}, {"LEMMA":"sąd"}, {"LOWER":"prawa"}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"ENT_TYPE":"PLACENAME"}]
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
        # landwójt + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # landwójt + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # landwójt + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # landwójt + 'm' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    # podwójt z + skrót miejscowości np.: A.
    for litera in litery:
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
