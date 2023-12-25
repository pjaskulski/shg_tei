""" definicja reguł dla wyszukiwania urzędów w SHG """
# cspell: disable


def rule_patterns_notariusze() -> list:
    """ definicje reguł """
    patterns = [
        # notariusz
        [{"LEMMA":"notariusz"}],
        # notariusz z + nazwa
        [{"LEMMA":"notariusz"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # notariusz miejski w + nazwa, przymiotnik + nazwa, w rzeczownik
        [{"LEMMA":"notariusz"}, {"LEMMA":"miejski"}, {"LOWER":"w"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"notariusz"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"notariusz"}, {"LOWER":"w"}, {"POS":"NOUN", "OP": "+"}],
        # notariusz z. sandomierskiej (przymiotnik)
        [{"LEMMA":"notariusz"}, {"LOWER":"z"}, {"IS_PUNCT":True}, {"POS":"ADJ"}],
        # notariusz + przymiotnik
        [{"LEMMA":"notariusz"}, {"POS":"ADJ"}],
        # notariusz + rzeczownik
        [{"LEMMA":"notariusz"}, {"POS":"NOUN", "OP":"+"}],
        # notariusz + rzeczownik + przymiotnik
        [{"LEMMA":"notariusz"}, {"POS":"NOUN"}, {"POS":"ADJ"}],
        # notariusz + król.
        [{"LEMMA":"notariusz"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        # notariusz + bpa
        [{"LEMMA":"notariusz"}, {"LOWER":"bpa"}],
        # notariusz i funkcja
        [{"LEMMA":"notariusz"}, {"LOWER":"i"}, {"POS":"NOUN"}],
        # notariusz + publ.
        [{"LEMMA":"notariusz"}, {"LOWER":"publ"}, {"IS_PUNCT":True}],
        # notariusz + kogo (np. Jana Długosza)
        [{"LEMMA":"notariusz"}, {"ENT_TYPE":"PROPN", "OP":"+"}],
        # notariusz + kogo (np. ks. Henryka)
        [{"LEMMA":"notariusz"}, {"LOWER":"ks"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP":"+"}],
        # notariusz w rzeczownik
        [{"LEMMA":"notariusz"}, {"LOWER":"w"}, {"POS":"NOUN", "OP":"+"}],
        # protonotariusz
        [{"LEMMA":"protonotariusz"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        [{"LEMMA":"protonotariusz"}, {"POS":"ADJ"}],
        [{"LEMMA":"protonotariusz"}, {"POS":"NOUN", "OP":"+"}],
        [{"LEMMA":"notariusz"}]
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
        # notariusz + skrót geogr.
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"z"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"bpa"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"publ"}, {"IS_PUNCT":True},
                         {"POS":"NOUN"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"POS":"NOUN"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LEMMA":"sąd"}, {"POS":"ADJ"},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"kap"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"woj"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"LOWER":"diec"},
                         {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    # notariusz z + skrót miejscowości np.: notariusz z A., notariusz A.
    for litera in litery:
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"ze"}, {"TEXT":f"{litera}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"POS":"ADJ"}, {"LOWER":"w"},
                         {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
