""" definicja reguł dla wyszukiwania urzędów w SHG """
# cspell: disable


def rule_patterns_podwojtowie() -> list:
    """ definicje reguł """
    patterns = [
        # podwójt + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"podwójt"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"POS":"ADJ", "OP": "+"}],
        # podwójt + przymiotnik i przymiotnik
        [{"LEMMA":"podwójt"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LOWER":"podwójci"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"podwójcina"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LOWER":"podwójcina"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # podwójt + nazwa własna (lub parę nazw)
        [{"LEMMA":"podwójt"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"podwójt"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt + rzeczownik
        [{"LEMMA":"podwójt"}, {"POS":"NOUN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"POS":"NOUN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"NOUN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"POS":"NOUN", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"POS":"NOUN", "OP": "+"}],
        # podwójt w nazwa (lub parę)
        [{"LEMMA":"podwójt"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt w + rzeczownik (lub parę)
        [{"LEMMA":"podwójt"}, {"LOWER":"w"}, {"POS":"NOUN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"w"}, {"POS":"NOUN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"w"}, {"POS":"NOUN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"w"}, {"POS":"NOUN", "OP": "+"}],
        # podwójt z nazwa
        [{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt z + rzeczownik
        [{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"POS":"NOUN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"z"}, {"POS":"NOUN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"POS":"NOUN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"POS":"NOUN", "OP": "+"}],
        # landwójt ze + nazwa
        [{"LOWER":"podwójci"}, {"LOWER":"ze"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"ze"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"ze"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt m. nazwa
        [{"LEMMA":"podwójt"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt miasta nazwa
        [{"LEMMA":"podwójt"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"LEMMA":"miasto"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt wsi nazwa
        [{"LEMMA":"podwójt"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt z wsi nazwa
        [{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"z"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"LOWER":"z"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt ze wsi nazwa
        [{"LEMMA":"podwójt"}, {"LOWER":"ze"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"ze"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"ze"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"ze"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        [{"LOWER":"podwójcina"}, {"LOWER":"ze"}, {"LEMMA":"wieś"},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # podwójt sądu wyższego pr. niem.
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True},
         {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True},
         {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # podwójt sądu leńskiego + nazwa (opcjonalnie - w)
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"w", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"w", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        # podwójt sądu leńskiego + nazwa (opcjonalnie - z)
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"z", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"z", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"z", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"z", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        # podwójt leńskiego sądu
        [{"LEMMA":"podwójt"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"LOWER":"w", "OP":"?"},
         {"ENT_TYPE":"PLACENAME"}],
        # podwójci wyższego sądu [prawa niem.]
        [{"LOWER":"podwójci"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"IS_PUNCT":True, "OP":"?"},
         {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LOWER":"podwójci"}, {"LEMMA":"wysoki"}, {"LEMMA":"sąd"}, {"IS_PUNCT":True, "OP":"?"},
         {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LOWER":"podwójci"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"IS_PUNCT":True, "OP":"?"},
         {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LOWER":"podwójci"}, {"LEMMA":"wysoki"}, {"LEMMA":"sąd"}, {"IS_PUNCT":True, "OP":"?"},
         {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # podwójt, podwójci
        [{"LEMMA":"podwójt"}],
        [{"LEMMA":"podwójci"}],
        [{"LOWER":"podwójci"}]
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
        # podwójt + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójcina"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # podwójt + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójcina"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        # podwójt + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójcina"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"},
                         {"IS_PUNCT":True}])
        # podwójt + 'm' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                         {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    # podwójt z + skrót miejscowości np.: A.
    for litera in litery:
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"w"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójt"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójt"}, {"LEMMA":"miasto"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LEMMA":"miasto"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                            {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"z"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                            {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"w"}, {"LOWER":"m"}, {"IS_PUNCT":True},
                            {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójcina"}, {"LOWER":"z"}, {"TEXT":f"{litera}"},
                            {"IS_PUNCT":True}])

    patterns_output = []
    for item in patterns:
        patterns_output.append({"label": "OCCUPATION_MUNICIPAL",
                        "pattern": item,
                        "id": "podwójt"})


    return patterns_output
