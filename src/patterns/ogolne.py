""" definicja reguł ogólnych w SHG """
# cspell: disable


def patterns_ogolne(obiekty:list, fizjografia:list, imiona:list, miejscowosci:list) -> list:
    """ definicje reguł """

    shortcuts = ["krak", "lel", "biec", "chęc", "czchow", "czech", "czes", "frank", "gnieźn",
                    "imbr", "jędrz", "kal", "Klar", "koprz", "ksiąs", "lub", "łęcz", "magd", "maz",
                    "miech", "miej", "mog", "mstow", "niem", "opocz", "ośw", "pilzn", "pol", "poł",
                    "pozn", "pras", "prosz", "przem", "rad", "roz", "san", "sand", "sądec",
                    "sieciech", "sier", "siew", "staniąt", "starosądec", "szczyrz", "śl", "średz",
                    "świętokrz", "świętop", "tyn", "wąch", "węg", "wiel", "wiśl", "wojn", "zator",
                    "zawich", "zwierzyn", "żarn", "żyd"]

    patterns = [
           # obiekty gospodarcze, budowle itp.
           {"label":"OBJECT",
            "pattern": [{"LEMMA": {"IN": obiekty}}],
            "id": "obj"
           },
           # obiekty fizjograficzne
           {"label":"FIZJOGRAFIA",
            "pattern": [{"LEMMA": {"IN": fizjografia}, "IS_TITLE": False}],
            "id": "fiz"
           },
           # staropolskie imiona
           {"label":"PERSON",
            "pattern": [{"LEMMA": {"IN": imiona}}],
            "id": "person"
           },
           # staropolskie miejscowosci
           {"label":"PLACENAME",
            "pattern": [{"LEMMA": {"IN": miejscowosci}}],
            "id": "placename"
           },
           # obiekty gosp. i budowle jako skróty
           {"label":"OBJECT",
            "pattern": [{"TEXT": {"IN": ["folw", "kat", "kl", "kol"]}}, {"IS_PUNCT": True}],
            "id": "obj"
           },
           # obiekty fizjograficzne jako skróty
           {"label":"FIZJOGRAFIA",
            "pattern": [{"TEXT": {"IN": ["jez", "rz"]}}, {"IS_PUNCT": True}],
            "id": "fiz"
           },
           # herby
           {"label":"COATOFARMS",
            "pattern": [{"TEXT": "h"}, {"IS_PUNCT": True}, {"POS": "PROPN"}]
           },
           # osoba z miejscowości
           {"label": "PERSON",
            "pattern": [{"ENT_TYPE": "PERSNAME", "OP":"+"}, {"TEXT": "z"},
                        {"ENT_TYPE":"PLACENAME"}],
            "id": "person_1"
           },
           {"label": "PERSON",
            "pattern": [{"ENT_TYPE": "PERSNAME", "OP":"+"}, {"TEXT": "ze"},
                        {"ENT_TYPE":"PLACENAME"}],
            "id": "person_3"
           },
           {"label": "PERSON",
            "pattern": [{"ENT_TYPE": "PERSNAME", "OP":"+"}, {"TEXT": "s"}, {"IS_PUNCT":True},
                        {"ENT_TYPE":"PERSNAME"}],
            "id": "person_3"
           },
           # plebani
           {"label": "OCCUPATION_CHURCH_LOW",
            "pattern": [{"LEMMA": "pleban"}, {"TEXT": {"IN": ["w", "z"]}}, {"ENT_TYPE": "PLACENAME"}],
            "id": "pleban"
           },
           {"label": "OCCUPATION_CHURCH_LOW",
            "pattern": [{"LEMMA": "pleban"}, {"LEMMA": "kościół"}, {"ENT_TYPE": "PLACENAME"}],
            "id": "pleban"
           },
           {"label": "OCCUPATION_CHURCH_LOW",
            "pattern": [{"LEMMA": "pleb"}, {"IS_PUNCT": True}, {"TEXT": {"IN": ["w", "z"]}},
                        {"ENT_TYPE": "PLACENAME"}],
            "id":"pleban"
           },
           {"label": "OCCUPATION_CHURCH_LOW",
            "pattern": [{"LEMMA": "pleb"}, {"IS_PUNCT": True}, {"LEMMA": "kościół"},
                        {"ENT_TYPE": "PLACENAME"}],
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
            "pattern": [{"LEMMA": "oficjał"}, {"POS":"ADJ", "OP": "*"}],
            "id": "oficjał"
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
           # urzędy ziemskie
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "burgrabia"}, {"POS":"ADJ", "OP": "*"}],
            "id": "burgrabia"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "burgrabia"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "burgrabia"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "celnik"}, {"POS":"ADJ", "OP": "*"}],
            "id": "celnik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "celnik"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "celnik"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "chorąży"}, {"POS":"ADJ", "OP": "*"}],
            "id": "chorąży"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "chorąży"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "chorąży"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "ciwun"}, {"POS":"ADJ", "OP": "*"}],
            "id": "ciwun"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "ciwun"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "ciwun"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "cześnik"}, {"POS":"ADJ", "OP": "*"}],
            "id": "cześnik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "cześnik"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "cześnik"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "generał"}, {"POS": "NOUN", "OP":"*"}, {"POS":"ADJ", "OP": "*"}],
            "id": "generał"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "hetman"}, {"POS":"ADJ", "OP": "*"}],
            "id": "hetman"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "horodniczy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "horodniczy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "horodniczy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "horodniczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "instygator"}, {"POS":"ADJ", "OP": "*"}],
            "id": "instygator"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "instygator"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "instygator"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "kanclerz"}, {"LEMMA": "koronny"}],
            "id": "kanclerz"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "kanclerz"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kanclerz"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "klucznik"}, {"POS":"ADJ", "OP": "*"}],
            "id": "klucznik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "klucznik"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "klucznik"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "konarski"}, {"POS":"ADJ", "OP": "*"}],
            "id": "konarski"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "konarski"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "konarski"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "koniuszy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "koniuszy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "koniuszy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "koniuszy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "korzenny"}, {"POS":"ADJ", "OP": "*"}],
            "id": "korzenny"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "korzenny"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "korzenny"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "krajczy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "krajczy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "krajczy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "krajczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "kuchmistrz"}, {"POS":"ADJ", "OP": "*"}],
            "id": "kuchmistrz"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "kuchmistrz"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "kuchmistrz"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "ławnik"}, {"LEMMA": "ziemski"}],
            "id": "ławnik"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "łożniczy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "łożniczy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "łożniczy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "łożniczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "łowczy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "łowczy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "łowczy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "łowczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "łowczy"}, {"TEXT": {"IN": ["lub", "krak", "sand", "lel"]}},
                         {"IS_PUNCT": True}],
            "id": "łowczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "marszałek"},
                         {"LEMMA": {"IN": ["dworski", "koronny", "nadworny", "wielki", "królestwo"]}}],
            "id": "marszałek"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "miecznik"}, {"POS":"ADJ", "OP": "*"}],
            "id": "miecznik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "miecznik"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "miecznik"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "mierniczy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "mierniczy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "mierniczy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "mierniczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "mostowniczy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "mostowniczy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "mostowniczy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "mostowniczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "pisarz"}, {"LEMMA":{"IN": ["skarbowy", "ziemski", "polny"]}}],
            "id": "pisarz"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "pocztmagister"}, {"POS":"ADJ", "OP": "*"}],
            "id": "pocztmagister"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "podczaszy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "podczaszy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podczaszy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podczaszy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "podkanclerzy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "podkanclerzy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podkanclerzy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podczaszy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "podkoni"}, {"POS":"ADJ", "OP": "*"}],
            "id": "podkoni"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podkoni"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podkoni"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podrzędczy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "podrzędczy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podrzędczy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podrzędczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "podłowczy"}, {"POS":"ADJ", "OP": "*"}],
            "id": "podłowczy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podłowczy"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podłowczy"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "podsędek"}, {"POS":"ADJ", "OP": "*"}],
            "id": "podsędek"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podsędek"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podsędek"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "podskarbi"}, {"POS":"ADJ", "OP": "*"}],
            "id": "podskarbi"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podskarbi"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podskarbi"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "podstoli"}, {"POS":"ADJ", "OP": "*"}],
            "id": "postoli"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podstoli"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podstoli"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "podstarości"}, {"POS":"ADJ", "OP": "*"}],
            "id": "podstarości"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "podstarości"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "podstarości"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "prefekt"}, {"POS":"ADJ", "OP": "*"}],
            "id": "prefekt"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "prefekt"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "prefekt"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "referendarz"}, {"POS":"ADJ", "OP": "*"}],
            "id": "referendarz"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "referendarz"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "referendarz"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "regent"}, {"POS":"ADJ", "OP": "*"}],
            "id": "regent"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "sekretarz"}, {"POS":"ADJ", "OP": "*"}],
            "id": "sekretarz"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "skarbnik"}, {"POS":"ADJ", "OP": "*"}],
            "id": "skarbnik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "skarbnik"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "skarbnik"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "skarbny"}, {"POS":"ADJ", "OP": "*"}],
            "id": "skarbny"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "starosta"}, {"POS":"ADJ", "OP": "*"}],
            "id": "starosta"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "starosta"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "starosta"
           },
           # star. + przymiotnik
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"TEXT": "star"},{"IS_PUNCT": True}, {"POS":"ADJ", "OP": "*"}],
            "id": "starosta"
           },
           # star. + skrót
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"TEXT": "star"},{"IS_PUNCT": True},
                         {"TEXT": {"IN": ["lub", "krak", "sand", "lel"]}},
                         {"IS_PUNCT": True}],
            "id": "starosta"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "stolnik"}, {"POS":"ADJ", "OP": "*"}],
            "id": "stolnik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "stolnik"}, {"LOWER": {"IN": shortcuts}},
                        {"IS_PUNCT":True}],
            "id": "stolnik"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "strażnik"}, {"POS":"ADJ", "OP": "*"}],
            "id": "strażnik"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "wiceinstygator"}, {"POS":"ADJ", "OP": "*"}],
            "id": "wiceinstygator"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "wiceregent"}, {"POS":"ADJ", "OP": "*"}],
            "id": "wiceregent"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "wicewojewoda"}, {"POS":"ADJ", "OP": "*"}],
            "id": "wicewojewoda"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "wicewojewoda"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "wicewojewoda"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "wielkorządca"}, {"TEXT": {"IN": ["krak", "sand"]}}, {"IS_PUNCT": True}],
            "id": "wielkorządca"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "wielkorządca"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "wielkorządca"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "włodarz"}, {"POS":"ADJ", "OP": "*"}],
            "id": "włodarz"
           },
           {"label":"OCCUPATION_LAND",
            "pattern":  [{"LEMMA": "wojski"}, {"POS":"ADJ", "OP": "*"}],
            "id": "wojski"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "wojski"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "wojski"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "woźny"}, {"POS":"ADJ", "OP": "*"}],
            "id": "woźny"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"LEMMA": "woźny"}, {"LOWER": {"IN": shortcuts}}, {"IS_PUNCT":True}],
            "id": "woźny"
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
           # skróty urzędów z kropkami: burgr., kaszt., komor., pkancl., pkom., prep. pstar.
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
            "pattern": [{"TEXT": "pstar"}, {"IS_PUNCT": True}, {"POS":"ADJ", "OP": "*"}],
            "id": "podstarości"
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
            "pattern": [{"TEXT": "kaszt"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}},
                        {"IS_PUNCT":True}],
            "id": "kasztelan"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "komor"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}},
                        {"IS_PUNCT":True}],
            "id": "komornik"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "pkancl"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}},
                        {"IS_PUNCT":True}],
            "id": "podkanclerzy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "pkom"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}},
                        {"IS_PUNCT":True}],
            "id": "podkomorzy"
           },
           {"label": "OCCUPATION_LAND",
            "pattern": [{"TEXT": "burgr"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}},
                        {"IS_PUNCT":True}],
            "id": "burgrabia"
           },
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "prep"}, {"IS_PUNCT": True}, {"LOWER": {"IN": shortcuts}},
                        {"IS_PUNCT":True}],
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

    # w zeszycie 1 z części V SHG występują tylko miejscowości na M i N
    # litery = 'ABCDEFGHIJKLMNOPRSTUWZŚŻŹĆŁ'
    litery = 'MN'

    # skróty miejscowości
    for litera in litery:
        patterns.append(
           {"label":"PLACENAME",
            "pattern": [{"TEXT":f"{litera}"}, {"IS_PUNCT":True}]
           })
        # osoba z bieżącej miejscowości
        patterns.append({"label": "PERSON",
            "pattern": [{"ENT_TYPE": "PERSNAME", "OP":"+"}, {"TEXT": "z"},
                        {"TEXT":f"{litera}"}, {"IS_PUNCT":True}],
            "id": "person_2"
           })
        # prep. kl. z M.
        patterns.append(
           {"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "prep"}, {"IS_PUNCT": True},{"TEXT":"kl"},
                        {"IS_PUNCT": True}, {"TEXT":"z"}, {"TEXT":f"{litera}"},
                        {"IS_PUNCT": True}],
            "id": "prepozyt"
           })
        # prep. w M.
        patterns.append({"label": "OCCUPATION_CHURCH_HIGH",
            "pattern": [{"TEXT": "prep"}, {"IS_PUNCT": True},
                        {"TEXT": {"IN":["w","z"]}}, {"TEXT":f"{litera}"},
                        {"IS_PUNCT": True}],
            "id": "prepozyt"
           })

    return patterns
