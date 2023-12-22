""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns_pisarze() -> list:
    """ definicje reguł """
    patterns = [
        # pisarz m. + nazwa
        [{"LEMMA":"pisarz"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # pisarz z + nazwa
        [{"LEMMA":"pisarz"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # pisarz w + nazwa
        [{"LEMMA":"pisarz"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # pisarz miejski + nazwa
        [{"LEMMA":"pisarz"}, {"LEMMA":"miejski"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # pisarz miej.
        [{"LEMMA":"pisarz"}, {"LOWER":"miej"}, {"IS_PUNCT":True}],
        # pisarz miej. + przymiotnik
        [{"LEMMA":"pisarz"}, {"LOWER":"miej"}, {"IS_PUNCT":True}, {"POS":"ADJ"}],
        # pisarz przymiotnik + nazwa
        [{"LEMMA":"pisarz"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # pisarz sądu wyższego pr. niem.
        [{"LEMMA":"pisarz"}, {"LEMMA":"sąd"}, {"LEMMA":"wysoki"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # pisarz + rzeczownik
        [{"LEMMA":"pisarz"}, {"POS":"NOUN", "OP":"+"}],
        # pisarz król.
        [{"LEMMA":"pisarz"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        # pisarz i dworzanin król.
        [{"LEMMA":"pisarz"}, {"LOWER":"i"}, {"POS":"NOUN"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        # pisarz kancelarii król.
        [{"LEMMA":"pisarz"}, {"POS":"NOUN"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        # pisarz star. + przymiotnik
        [{"LEMMA":"pisarz"}, {"LOWER":"star"}, {"IS_PUNCT":True}, {"POS":"ADJ"}],
        # pisarz sądu + przymiotnik
        [{"LEMMA":"pisarz"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}],
        [{"LEMMA":"pisarz"}]
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
        # pisarz + skrót geogr.
        patterns.append([{"LEMMA":"pisarz"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LEMMA":"miejski"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"POS":"ADJ"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"POS":"NOUN"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"POS":"ADJ"}, {"LOWER":"ziemi"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LEMMA":"sędzia"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"bpów"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LEMMA":"kapituła"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    # pisarz z + skrót miejscowości np.: pisarz z A., pisarz A.
    for litera in litery:
        patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LEMMA":"miejski"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"POS":"ADJ"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"w"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
