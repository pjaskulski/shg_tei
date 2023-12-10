""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns_lawnicy() -> list:
    """ definicje reguł """
    patterns = [
        # ławnik + przymiotnik (lub parę przymiotników)
        # opcjonalnie 'sądu leńskiego'
        [{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"POS":"ADJ", "OP": "+"}],
        # ławnik + przymiotnik i przymiotnik
        [{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # ławnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # ławnik + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # ławnik + rzeczownik
        [{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"POS":"NOUN"}],
        # ławnik w nazwa (lub parę)
        [{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # ławnik z nazwa
        [{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"LOWER":"z"}, {"ENT_TYPE":"ENT_TYPE", "OP": "+"}],
        # ławnik m. nazwa
        [{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],

        # ławnik sądu najwyższego pr. niem. na zamku krak.
        [{"TEXT":"ławnik sądu najwyższego pr. niem. na zamku krak."}],
        # ławnik sądu wyższego pr. niem. w + nazwa (klasztor, zamek, miasto)
        # ławnik sądu pr. niem. w + nazwa
        [{"LEMMA":"ławnik"}, {"LEMMA":"sąd"}, {"POS":"ADJ", "OP":"?"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME"}],
        # ławnik sądu pr. niem. na zamku krak
        [{"LEMMA":"ławnik"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"na"}, {"LEMMA":"zamek"}, {"LOWER":"krak"}],
        # ławnik sądu wyż. pr. niem. w + nazwa
        [{"LEMMA":"ławnik"}, {"LEMMA":"sąd"}, {"LOWER":"wyż"}, {"IS_PUNCT":True}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME"}],
        # ławnik sądu gajonego + nazwa
        [{"LEMMA":"ławnik"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"ławnik"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME"}],
        # ławnik sądu landwójta
        [{"LEMMA":"ławnik"}, {"LEMMA":"sąd"}, {"LEMMA":"landwójt"}],
        # ławnik wsi
        [{"LEMMA":"ławnik"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP":"?"}],
        # przysiężny w + nazwa
        [{"LEMMA":"przysiężny"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME"}],
        # przysiężny z + nazwa
        [{"LEMMA":"przysiężny"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME"}],
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
        # ławnik + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # ławnik + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # ławnik + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # ławnik sądu ziemskiego + skrót geogr.
        patterns.append([{"LEMMA":"ławnik"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    # ławnik, ławnicy z + skrót miejscowości np.: A.
    for litera in litery:
        patterns.append([{"LEMMA":"ławnik"}, {"LOWER":"sądu", "OP":"?"}, {"LOWER":"leńskiego", "OP":"?"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
