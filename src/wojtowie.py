""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns_wojtowie() -> list:
    """ definicje reguł """
    patterns = [
        # wójt + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"wójt"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"POS":"ADJ", "OP": "+"}],
        # wójt + przymiotnik i przymiotnik
        [{"LEMMA":"wójt"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"wójtowy"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"wójcina"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # wójt + nazwa własna (lub parę nazw)
        [{"LEMMA":"wójt"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wójt + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"wójt"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wójt + rzeczownik
        [{"LEMMA":"wójt"}, {"POS":"NOUN"}],
        [{"LEMMA":"wójtowy"}, {"POS":"NOUN"}],
        [{"LEMMA":"wójcina"}, {"POS":"NOUN"}],
        # wójt w nazwa (lub parę)
        [{"LEMMA":"wójt"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wójt z nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wójt m. nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wójt wsi nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wójt z wsi nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wójt ze wsi nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # wójt sądu najwyższego pr. niem. na zamku krak.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"na"}, {"LEMMA":"zamek"}, {"LOWER":"krak"}, {"IS_PUNCT":True}],
        # wójt sądu pr. niem. w kluczu łąckim
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"LEMMA":"klucz"}, {"POS":"ADJ"}],
        # wójt sądu wyższego dworskiego kl. miech.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ", "OP":"+"}, {"LOWER":"kl"}, {"IS_PUNCT":True}, {"LOWER":"miech"}, {"IS_PUNCT":True}],
        # wójt sądu najw. pr. niem. na zamku krak.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"LOWER":"najw"}, {"IS_PUNCT":True}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"na"}, {"LEMMA":"zamek"}, {"LOWER":"krak"}, {"IS_PUNCT":True}],
        # wójt sądu wyższego pr. niem. w + nazwa (klasztor, zamek, miasto)
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP":"+"}],
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP":"+"}],
        # wójt sądu leńskiego w + nazwa
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"POS":"PROPN", "OP":"+"}],
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"POS":"NOUN", "OP":"+"}],
        # wójt sądu wyższego dworskiego pr. niem. + nazwa
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP":"+"}],
        # wójt sądu wyższego pr. niem. magd.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"magd"}, {"IS_PUNCT":True}],
        # wójt sądu prawa niem.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # wójt sądu wyższego prawa niem.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # wójt i mieszcz. z nazwa, wójt i mieszczanin z nazwa, wójt i mieszcz. nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"i"}, {"LEMMA":"mieszcz"}, {"IS_PUNCT":True}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"wójt"}, {"LOWER":"i"}, {"LEMMA":"mieszczanin"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"wójt"}, {"LOWER":"i"}, {"LEMMA":"mieszcz"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"wójt"}, {"LOWER":"i"}, {"LEMMA":"mieszczanin"}, {"ENT_TYPE":"PLACENAME"}],
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
        # wójt + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # wójt + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # wójt + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

        # wójt + 'm' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    # wójt z + skrót miejscowości np.: A.
    for litera in litery:
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
