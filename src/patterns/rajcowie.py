""" definicja reguł dla wyszukiwania urzędów w SHG """
# cSpell:disable


# rajca + przymiotnik (lub parę przymiotników) np. rajca krakowski
# rajca + przymiotnik i przymiotnik np. rajcy starzy i nowi
# rajca + nazwa własna (lub parę nazw) np. rajca Wiślicy
# rajca + skrót (geograficzny) np rajca krak., rajcy biec. rajców lel.
# rajca w nazwa np. rajca w Wiślicy
# rajca z nazwa np. rajca z Wiślicy
# rajca m. nazwa np. rajca m. Wiślicy

def rule_patterns_rajcowie() -> list:
    """ definicje reguł """
    patterns = [
        # rajca
        [{"LEMMA":"rajca"}],
        # rajca + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"rajca"}, {"POS":"ADJ", "OP": "+"}],
         # rajca + przymiotnik i przymiotnik
        [{"LEMMA":"rajca"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # rajca + nazwa własna (lub parę nazw)
        [{"LEMMA":"rajca"}, {"ENT_TYPE":"PLACENAME", "OP": "*"}],
        # rajca + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"rajca"}, {"POS":"ADJ"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # rajca w nazwa (lub parę)
        [{"LEMMA":"rajca"}, {"LOWER":"w"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
        # rajca z nazwa
        [{"LEMMA":"rajca"}, {"LOWER":"z"}, {"ENT_TYPE":"PLACENAME", "OP": "+"}],
         # rajca m. nazwa
        [{"LEMMA":"rajca"}, {"LOWER":"m"}, {"IS_PUNCT":True},
         {"ENT_TYPE":"PLACENAME", "OP": "+"}],
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
        # rajca, rajcy + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"rajca"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

    for litera in litery:
        patterns.append([{"LEMMA":"rajca"}, {"LOWER": {"IN": ["w", "z"]}},
                         {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    patterns_output = []
    for item in patterns:
        patterns_output.append({"label": "OCCUPATION_MUNICIPAL",
                                "pattern": item,
                                "id": "rajca"})

    return patterns_output
