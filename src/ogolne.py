""" definicja reguł ogólnych w SHG """


def patterns_ogolne(skrot:str, obiekty:list, fizjografia:list) -> list:
    """ definicje reguł """

    shortcuts = ["krak", "lel", "biec", "chęc", "czchow", "czech", "czes", "frank", "gnieźn",
                    "imbr", "jędrz", "kal", "Klar", "koprz", "ksiąs", "lub", "łęcz", "magd", "maz",
                    "miech", "miej", "mog", "mstow", "niem", "opocz", "ośw", "pilzn", "pol", "poł",
                    "pozn", "pras", "prosz", "przem", "rad", "roz", "san", "sand", "sądec",
                    "sieciech", "sier", "siew", "staniąt", "starosądec", "szczyrz", "śl", "średz",
                    "świętokrz", "świętop", "tyn", "wąch", "węg", "wiel", "wiśl", "wojn", "zator",
                    "zawich", "zwierzyn", "żarn", "żyd"]

    patterns = [
           {"label":"OBJECT",
            "pattern": [{"LEMMA": {"IN": obiekty}}],
            "id": "obj"
           },
           {"label":"FIZJOGRAFIA",
            "pattern": [{"LEMMA": {"IN": fizjografia}}],
            "id": "fiz"
           },
           {"label":"COATOFARMS",
            "pattern": [{"TEXT": "h"}, {"IS_PUNCT": True}, {"POS": "PROPN"}]
           },
           {"label":"PLACENAME",
            "pattern": [{"TEXT":f"{skrot}"}, {"IS_PUNCT":True}]
           },
           {"label": "PERSON",
            "pattern": [{"ENT_TYPE": "PERSNAME", "OP":"+"}, {"TEXT": "z"}, {"ENT_TYPE":"PLACENAME"}],
            "id": "person_1"
           },
           {"label": "PERSON",
            "pattern": [{"ENT_TYPE": "PERSNAME", "OP":"+"}, {"TEXT": "z"}, {"TEXT":f"{skrot}"}, {"IS_PUNCT":True}],
            "id": "person_2"
           },
           {"label": "PERSON",
            "pattern": [{"ENT_TYPE": "PERSNAME", "OP":"+"}, {"TEXT": "ze"}, {"ENT_TYPE":"PLACENAME"}],
            "id": "person_3"
           },
           {"label": "PERSON",
            "pattern": [{"ENT_TYPE": "PERSNAME", "OP":"+"}, {"TEXT": "s"}, {"IS_PUNCT":True}, {"ENT_TYPE":"PERSNAME"}],
            "id": "person_3"
           },
           # plebani
           {"label": "OCCUPATION_CHURCH_LOW",
            "pattern": [{"LEMMA": "pleban"}, {"TEXT": "w"}, {"ENT_TYPE": "PLACENAME"}],
            "id": "pleban"
           },
           {"label": "OCCUPATION_CHURCH_LOW",
            "pattern": [{"LEMMA": "pleban"}, {"LEMMA": "kościół"}, {"ENT_TYPE": "PLACENAME"}],
            "id": "pleban"
           },
           {"label": "OCCUPATION_CHURCH_LOW",
            "pattern": [{"LEMMA": "pleb"}, {"IS_PUNCT": True}, {"TEXT": "w"}, {"ENT_TYPE": "PLACENAME"}],
            "id":"pleban"
           },
           {"label": "OCCUPATION_CHURCH_LOW",
            "pattern": [{"LEMMA": "pleb"}, {"IS_PUNCT": True}, {"LEMMA": "kościół"}, {"ENT_TYPE": "PLACENAME"}],
            "id": "pleban"
           },
           # wyższe kościelne
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "arcybiskup"}, {"POS":"ADJ", "OP": "*"}],
            "id":"arcybiskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "abp"}, {"POS":"ADJ", "OP": "*"}],
            "id": "arcybiskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "arcbp"}, {"POS":"ADJ", "OP": "*"}],
            "id": "arcybiskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "biskup"}, {"POS":"ADJ", "OP": "*"}],
            "id": "biskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "bp"}, {"POS":"ADJ", "OP": "*"}],
            "id": "biskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "dziekan"}, {"POS":"ADJ", "OP": "*"}],
            "id": "dziekan"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kanonik"}, {"POS":"ADJ", "OP": "*"}],
            "id": "kanonik"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kanclerz"}, {"POS":"ADJ", "OP": "*"}],
            "id": "kanclerz"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kleryk"}, {"POS":"ADJ", "OP": "*"}],
            "id": "kleryk"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kantor"}, {"POS":"ADJ", "OP": "*"}],
            "id": "kantor"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "komandor"}, {"POS":"ADJ", "OP": "*"}],
            "id": "komandor"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kustosz"}, {"POS":"ADJ", "OP": "*"}],
            "id": "kustosz"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "prałat"}, {"POS":"ADJ", "OP": "*"}],
            "id": "prałat"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "prepozyt"}, {"POS":"ADJ", "OP": "*"}],
            "id": "prepozyt"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "scholastyk"}, {"POS":"ADJ", "OP": "*"}],
            "id": "scholastyk"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "sufragan"}, {"POS":"ADJ", "OP": "*"}],
            "id": "sufragan"
           },
           # skróty urzędów bez kropek
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "wwda"}, {"POS":"ADJ", "OP": "*"}],
            "id": "wojewoda"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "klan"}, {"POS":"ADJ", "OP": "*"}],
            "id": "kasztelan"
           },
           # skróty urzędów bez kropek + skróty geograficzne
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "wwda"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "wojewoda"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "klan"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kasztelan"
           },
           # skróty urzędów z kropkami: burgr., kaszt., komor., pkancl., pkom., prep.
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "kaszt"}, {"IS_PUNCT": True}, {"POS":"ADJ", "OP": "*"}],
            "id": "kasztelan"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "komor"}, {"IS_PUNCT": True}, {"POS":"ADJ", "OP": "*"}],
            "id": "komornik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "pkancl"}, {"IS_PUNCT": True}, {"POS":"ADJ", "OP": "*"}],
            "id": "podkanclerzy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "pkom"}, {"IS_PUNCT": True}, {"POS":"ADJ", "OP": "*"}],
            "id": "podkomorzy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "burgr"}, {"IS_PUNCT": True}, {"POS":"ADJ", "OP": "*"}],
            "id": "burgrabia"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "prep"}, {"IS_PUNCT": True}, {"POS":"ADJ", "OP": "*"}],
            "id": "prepozyt"
           },
           # skróty urzędów z kropkami + skróty geograficzne
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "kaszt"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kasztelan"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "komor"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "komornik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "pkancl"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podkanclerzy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "pkom"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podkomorzy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "burgr"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "burgrabia"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "prep"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "prepozyt"
           },
           # urzędy kościelne + skróty geo
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "arcybiskup"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "arcybiskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "abp"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "arcybiskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "arcbp"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "arcybiskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "biskup"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "biskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "bp"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "biskup"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "dziekan"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "dziekan"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kanonik"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kanonik"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kanclerz"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kanclerz"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kleryk"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kleryk"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kantor"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kantor"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "komandor"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "komandor"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "kustosz"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kustosz"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "prałat"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "prałat"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "prepozyt"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "prepozyt"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "scholastyk"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "scholastyk"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"LEMMA": "sufragan"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "sufragan"
           }
        ]

    return patterns
