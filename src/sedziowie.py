""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns_sedziowie() -> list:
    """ definicje reguł """
    patterns = [
        # sędzia + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"sędzia"}, {"POS":"ADJ", "OP":"+"}],
        # sędzia + przymiotnik (lub parę przymiotników) + kropka
        [{"LEMMA":"sędzia"}, {"POS":"ADJ", "OP":"+"}, {"IS_PUNCT": True}],
        # sędzia + przymiotnik i przymiotnik
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # sędzia + nazwa własna (lub parę nazw)
        [{"LEMMA":"sędzia"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia + rzeczownik (lub parę)
        [{"LEMMA":"sędzia"}, {"POS":"NOUN", "OP":"+"}],
        # sędzia w nazwa (lub parę nazw)
        [{"LEMMA":"sędzia"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia z nazwa (lub parę nazw)
        [{"LEMMA":"sędzia"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia m. nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia miasta nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia w mieście nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"w"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia wsi nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia z wsi nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia ze wsi nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia we wsi nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"we"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # sędzia sądu wyższego pr. niem. na + nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"na"}, {"ENT_TYPE":"PLACENAME"}],
        # sędzia sądu leńskiego na + nazwa (lub w + nazwa)
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"na"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"LOWER":"na"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"na"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME"}],
        # sędzia sądu leńskiego + przymiotnik
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"POS":"ADJ"}],
        # sędzia sądu pr. niem. + nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME"}],
        # sędzia sądu wyższego dworskiego pr. niem.
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # sędzia sądu wyższego dworskiego + nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"wysoki"}, {"LEMMA":"dworski"}, {"ENT_TYPE":"PLACENAME"}],
        # sędzia sądu wyższego dworskiego
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP":"?"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP":"?"}],
        # sędzia sądu sołeckiego
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"sołecki"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LOWER":"sołeckiego"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}],

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
        # sędzia + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sędzia"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia + 'm' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia sądu leńskiego na + rzeczownik + skrót (geograficzny)
        patterns.append([{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"na"}, {"POS":"NOUN"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia sądu + przymiotnik + skrót geogr.
        patterns.append([{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        
        # sędzia z + skrót miejscowości np.: A.
        for litera in litery:
            patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ", "OP":"+"}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ", "OP":"+"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
