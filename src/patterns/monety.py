""" definicja reguł dla wyszukiwania monet w SHG """
# cspell: disable


def rule_patterns_coin() -> list:
    """ definicje reguł """
    patterns = [
        # brakteat
        {"label": "COIN",
        "pattern": [{"LOWER":"brakteat"}],
        "id": "brakteat"
        },
        # denar
        {"label": "COIN",
         "pattern": [{"LEMMA":"denar"}],
         "id": "denar"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "den"}, {"IS_PUNCT": True}],
         "id": "denar"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA":"obol"}],
         "id": "denar"
        },
        # denar koloński
        {"label": "COIN",
         "pattern": [{"LEMMA":"denar"}, {"LEMMA": "koloński"}],
         "id": "denar_koloński"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA":"denar"}, {"TEXT": "kol"}, {"IS_PUNCT": True}],
         "id": "denar_koloński"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"den"}, {"IS_PUNCT": True}, {"TEXT": "kol"}, {"IS_PUNCT": True}],
         "id": "denar_koloński"
        },
        # denar krzyżowy
        {"label": "COIN",
         "pattern": [{"LEMMA":"denar"}, {"LEMMA": "krzyżowy"}],
         "id": "denar_krzyżowy"
        },
        # denar litewski
        {"label": "COIN",
         "pattern": [{"LEMMA":"denar"}, {"LEMMA": "litewski"}],
         "id": "denar_litewski"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA":"denar"}, {"TEXT": "lit"}, {"IS_PUNCT": True}],
         "id": "denar_litewski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"den"}, {"IS_PUNCT": True}, {"TEXT": "lit"}, {"IS_PUNCT": True}],
         "id": "denar_litewski"
        },
        # denar pruski
        {"label": "COIN",
         "pattern": [{"LEMMA":"denar"}, {"LEMMA": "chełmski"}],
         "id": "denar_pruski"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA":"denar"}, {"TEXT": "chełm"}, {"IS_PUNCT": True}],
         "id": "denar_pruski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"den"}, {"IS_PUNCT": True}, {"TEXT": "chełm"}, {"IS_PUNCT": True}],
         "id": "denar_pruski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"den"}, {"IS_PUNCT": True}, {"LEMMA": "pruski"}],
         "id": "denar_pruski"
        },
        # floren
        {"label": "COIN",
         "pattern": [{"LEMMA":"dukat"}],
         "id": "floren"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA":"floren"}],
         "id": "floren"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"fl"}, {"IS_PUNCT": True}],
         "id": "floren"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}],
         "id": "floren"
        },
        # floren litewski
        {"label": "COIN",
         "pattern": [{"TEXT":"fl"}, {"IS_PUNCT": True}, {"LEMMA": "litewski"}],
         "id": ""
        },
        # floren monety polskiej
        {"label": "COIN",
         "pattern": [{"TEXT":"fl"}, {"IS_PUNCT": True}, {"LEMMA": "moneta"}, {"LEMMA":"polski"}],
         "id": "floren_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"fl"}, {"IS_PUNCT": True}, {"LEMMA":"obiegowy"}, {"LEMMA": "moneta"},
                     {"LEMMA":"polska"}],
         "id": "floren_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"fl"}, {"IS_PUNCT": True}, {"LEMMA":"polski"}],
         "id": "floren_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}, {"LEMMA": "obiegowa"}, {"LEMMA":"moneta"}],
         "id": "floren_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}, {"LEMMA": "polski"}, {"LEMMA":"moneta"}],
         "id": "floren_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}, {"TEXT": "w"}, {"LEMMA":"bieżącej"}, {"LEMMA":"moneta"}],
         "id": "floren_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}, {"TEXT": "pol"}, {"IS_PUNCT":True}],
         "id": "floren_monety_polskiej"
        },
        # floren_monety_slaskiej
        {"label": "COIN",
         "pattern": [{"TEXT":"fl"}, {"IS_PUNCT": True}, {"LEMMA":"moneta"}, {"TEXT": "śl"},
                     {"IS_PUNCT": True}],
         "id": "floren_monety_slaskiej"
        },
        # floren półgroszy
        {"label": "COIN",
         "pattern": [{"TEXT":"fl"}, {"IS_PUNCT": True}, {"TEXT":"półgr"}, {"IS_PUNCT": True}],
         "id": "floren_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"fl"}, {"IS_PUNCT": True}, {"TEXT":"w"}, {"TEXT":"półgr"},
                     {"IS_PUNCT": True}],
         "id": "floren_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}, {"TEXT":"półgr"}, {"IS_PUNCT": True}],
         "id": "floren_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}, {"TEXT":"w"}, {"TEXT":"półgr"}, {"LEMMA": "stary"}],
         "id": "floren_polgroszy"
        },
        # floren_pruski
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}, {"LEMMA":"pruski"}],
         "id": "floren_pruski"
        },
        # floren renski
        {"label": "COIN",
         "pattern": [{"TEXT":"zł"}, {"LEMMA":"reński"}],
         "id": "floren_renski"
        },
        # floren_wegierski
        {"label": "COIN",
         "pattern": [{"LEMMA": "czerwony"}, {"TEXT":"fl"}, {"IS_PUNCT": True},
                     {"TEXT":"węg", "OP": "?"}, {"IS_PUNCT": True, "OP": "?"}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "czerwony"}, {"TEXT":"zł"}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "dukat"}, {"TEXT":"w"}, {"LEMMA": "złoto"}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": {"IN": ["dukat", "floren"]}}, {"TEXT":"węg"}, {"IS_PUNCT": True}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "fl"}, {"IS_PUNCT": True}, {"LEMMA": "czerwony"}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "fl"}, {"IS_PUNCT": True}, {"TEXT": "w"}, {"LEMMA": "złoto"}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "fl"}, {"IS_PUNCT": True}, {"TEXT": "węg"}, {"IS_PUNCT": True}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "fl"}, {"IS_PUNCT": True}, {"LEMMA": "węgierski"}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "zł"}, {"LEMMA": {"IN": ["czerwony", "węgierski"]}}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "zł"}, {"TEXT": "w"}, {"LEMMA":"czysty", "OP":"?"},
                     {"LEMMA": "złoto"}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "zł"}, {"TEXT": "węg"}, {"IS_PUNCT": True}],
         "id": "floren_wegierski"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "złoty"}, {"TEXT": "fl"}, {"IS_PUNCT": True}],
         "id": "floren_wegierski"
        },
        # grosz
        {"label": "COIN",
         "pattern": [{"LOWER": "gr"}],
         "id": "grosz"
        },
        # grosz_czeski
        {"label": "COIN",
         "pattern": [{"LOWER": "gr"}, {"LEMMA": {"IN": ["czeski", "praski", "szeroki"]}}],
         "id": "grosz_czeski"
        },
        {"label": "COIN",
         "pattern": [{"LOWER": "gr"}, {"TEXT": {"IN": ["czes", "pras", "szer"]}},
                     {"IS_PUNCT": True}],
         "id": "grosz_czeski"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "szer"}, {"IS_PUNCT": True}, {"TEXT": {"IN": ["czes", "pras"]}},
                     {"IS_PUNCT": True}],
         "id": "grosz_czeski"
        },
        # grosz litewski
        {"label": "COIN",
         "pattern": [{"TEXT": "gr"}, {"TEXT": "lit"}, {"IS_PUNCT": True}],
         "id": "grosz_litewski"
        },
        # grosz_monety_polskiej
        {"label": "COIN",
         "pattern": [{"TEXT": "gr"}, {"TEXT": "krak"}, {"IS_PUNCT": True}],
         "id": "grosz_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "gr"}, {"LEMMA": "krakowski"}],
         "id": "grosz_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "gr"}, {"LEMMA": "moneta"},
                     {"LEMMA": {"IN": ["bieżący","obiegowy","pospolity"]}}],
         "id": "grosz_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "gr"}, {"LEMMA": "moneta"}, {"TEXT": {"IN":["krak", "posp"]}},
                     {"IS_PUNCT": True}],
         "id": "grosz_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "gr"}, {"LEMMA": {"IN": ["polski","obiegowy","pospolity"]}}],
         "id": "grosz_monety_polskiej"
        },
        # moneta_grosz_polgroszy
        {"label": "COIN",
         "pattern": [{"TEXT":"gr"}, {"LEMMA": "dobry"}, {"TEXT": "półgr"}],
         "id": "grosz_półgroszy"
        },
        # grzywna
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True, "OP": "?"}],
         "id": "grzywna"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True, "OP": "?"}, {"LEMMA": "różny"},
                     {"LEMMA": "moneta"}],
         "id": "grzywna"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True, "OP": "?"}, {"LEMMA": "gotowy"},
                     {"LEMMA": "pieniądz"}],
         "id": "grzywna"
        },
        # grzywna_denarów
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "den"}, {"IS_PUNCT": True}],
         "id": "grzywna_denarów"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True},
                     {"LEMMA": {"IN": ["drobny", "lekki", "mały"]}},
                     {"LEMMA": {"IN":["moneta", "pieniądz"]}}],
         "id": "grzywna_denarów"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True},
                     {"LEMMA": {"IN": ["drobny", "lekki", "mały"]}},
                     {"TEXT": "den"}, {"IS_PUNCT": True}],
         "id": "grzywna_denarów"
        },
        # grzywna groszy
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA": "dobry", "OP":"?"},
                     {"TEXT": "gr"}],
         "id": "grzywna_groszy"
        },
        # grzywna_groszy_czeskich
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "gr"},
                     {"TEXT": {"IN": ["czes", "pras"]}}, {"IS_PUNCT": True}],
         "id": "grzywna_groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "gr"},
                     {"TEXT": {"IN": ["czeskich", "praskich"]}}],
         "id": "grzywna_groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True},
                     {"TEXT": {"IN": ["czeskich", "praskich"]}}],
         "id": "grzywna_groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True},
                     {"TEXT": "szer"}, {"IS_PUNCT":True},
                     {"TEXT": {"IN": ["czeskich", "praskich"]}}],
         "id": "grzywna_groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True},
                     {"LEMMA": "szeroki"}, {"IS_PUNCT":True},
                     {"TEXT": {"IN": ["czeskich", "praskich"]}}],
         "id": "grzywna_groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "w"}, {"TEXT": "gr"},
                     {"LEMMA": "praski"}],
         "id": "grzywna_groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "w"}, {"LEMMA": "grosz"}],
         "id": "grzywna_groszy_czeskich"
        },
        # grzywna_misnienska
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA":"miśnieński"}],
         "id": "grzywna_misnienska"
        },
        # grzywna_monety_polskiej
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA":"dobry"}, {"LEMMA": "moneta"},
                     {"LEMMA":"polski", "OP":"?"}],
         "id": "grzywna_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT":"gr"},
                     {"LEMMA": {"IN":["polski", "pospolity", "obiegowy"]}}],
         "id": "grzywna_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA": "lepszy"}, {"LEMMA": "moneta"}],
         "id": "grzywna_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA": "moneta"},
                     {"LEMMA": {"IN":["polski", "pospolity", "obiegowy", "drobny"]}}],
         "id": "grzywna_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": {"IN":["krak", "posp"]}},
                     {"IS_PUNCT": True}, {"TEXT":"gr", "OP":"?"}],
         "id": "grzywna_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True},
                     {"LEMMA":{"IN":["lepszy","pospolity", "wspólny", "zwykły"]}},
                     {"LEMMA":"moneta"}],
         "id": "grzywna_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT":"w"},
                     {"LEMMA":{"IN": ["bieżący", "drobny"]}}, {"LEMMA": "moneta"}],
         "id": "grzywna_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT":"w"}, {"LEMMA": "moneta"},
                     {"LEMMA":{"IN": ["bieżący", "drobny"]}}],
         "id": "grzywna_monety_polskiej"
        },
        # grzywna_polgroszy
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA": "kwartnik"}],
         "id": "grzywna_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "półgr"}],
         "id": "grzywna_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "półgr"},
                     {"LEMMA":"lepszy", "OP":"?"}, {"LEMMA":"moneta"},
                     {"TEXT":"krak"}, {"IS_PUNCT": "?"}],
         "id": "grzywna_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "półgr"},
                     {"TEXT":{"IN": ["pol", "szer"]}}, {"IS_PUNCT": "?"}],
         "id": "grzywna_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT": "szer"}, {"IS_PUNCT": True},
                     {"LEMMA":"kwartnik"}],
         "id": "grzywna_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA": "średni"}, {"TEXT": "gr"}],
         "id": "grzywna_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"TEXT":"w"}, {"LEMMA": "kwartnik"}],
         "id": "grzywna_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA":"wielki"},
                     {"LEMMA": "kwartnik"}],
         "id": "grzywna_polgroszy"
        },
        # grzywna_srebra
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True},
                     {"LEMMA": {"IN": ["czyste", "lane"]}, "OP":"?"}, {"LEMMA": "serbro"}],
         "id": "grzywna_srebra"
        },
        # grzywna_pruska
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA": "pruski"}],
         "id": "grzywna_pruska"
        },
        # grzywna_wegierska
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA": "węgierski"}],
         "id": "grzywna_wegierska"
        },
        # grzywna_torunska
        {"label": "COIN",
         "pattern": [{"TEXT": "grz"}, {"IS_PUNCT": True}, {"LEMMA": "toruński"}],
         "id": "grzywna_torunska"
        },
        # kopa
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}],
         "id": "kopa"
        },
        # kopa gr
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT": "gr"}],
         "id": "kopa_groszy"
        },
        # kopa_groszy_czeskich
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT": "gr"}, {"TEXT":"pras"}, {"IS_PUNCT":True}],
         "id": "groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"},{"TEXT":"w"}, {"TEXT": "szer"}, {"IS_PUNCT": True},
                     {"TEXT": "gr"}, {"TEXT":"czes"}, {"IS_PUNCT":True}],
         "id": "groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT": "gr"}, {"TEXT": "szer"}, {"IS_PUNCT": True},
                     {"TEXT":"pras"}, {"IS_PUNCT":True}],
         "id": "groszy_czeskich"
        },
        # kopa_groszy_monety_polskiej
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT": "gr"}, {"LEMMA": "moneta"},
                     {"LEMMA":{"IN":["bieżący", "pospolity"]}}],
         "id": "kopa_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"LEMMA": "moneta"}, {"TEXT": "krak"}, {"IS_PUNCT": True}],
         "id": "kopa_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"LEMMA": "moneta"}, {"LEMMA": "obiegowy"}],
         "id": "kopa_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT":"w"}, {"LEMMA": "moneta"}, {"LEMMA": "pospolity"}],
         "id": "kopa_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT":"zł"}, {"LEMMA": "polski"}],
         "id": "kopa_groszy_monety_polskiej"
        },
         {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT":"zł"}, {"TEXT": "pol"}, {"IS_PUNCT": True}],
         "id": "kopa_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT":"gr"}, {"IS_PUNCT": True},
                     {"LEMMA": "moneta"}, {"LEMMA": "pospolity"}],
         "id": "kopa_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"LEMMA":"moneta"}, {"LEMMA": "obiegowy"}],
         "id": "kopa_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT": "w"}, {"LEMMA":"moneta"}, {"LEMMA": "pospolity"}],
         "id": "kopa_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT": "gr"}, {"TEXT": "posp"}, {"IS_PUNCT": True}],
         "id": "kopa_groszy_monety_polskiej"
        },
        # kopa_groszy_w_szelagach
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT":"gr"}, {"TEXT": "w"}, {"LEMMA":"szeląg"}],
         "id": "kopa_groszy_w_szelagach"
        },
        # kopa_polgroszy
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"LEMMA":"kwartnik"}],
         "id": "kopa_polgroszy"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT":"półgr"}],
         "id": "kopa_polgroszy"
        },
        # kopa_szelagow_pruskich
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"TEXT":"gr"}, {"LEMMA":"szeląg"}, {"TEXT": "prus"},
                     {"IS_PUNCT": True}],
         "id": "kopa_szelagow_pruskich"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA": "kopa"}, {"LEMMA":"szeląg"}, {"LEMMA": "pruski"}],
         "id": "kopa_szelagow_pruskich"
        },
        # nobel
        {"label": "COIN",
         "pattern": [{"LEMMA": "nobel"}],
         "id": "nobel"
        },
        # nowe_fl
        {"label": "COIN",
         "pattern": [{"LEMMA": "nowy"}, {"TEXT":"fl"}, {"IS_PUNCT": True}],
         "id": "nowe_fl"
        },
        # ort
        {"label": "COIN",
         "pattern": [{"LOWER": "ort"}],
         "id": "ort"
        },
        # pieniadze
        {"label": "COIN",
         "pattern": [{"LEMMA": "pieniądz"}, {"LEMMA": "złoty"}, {"TEXT":"i"}, {"LEMMA":"srebrny"}],
         "id": "pieniadze"
        },
        # polgrosz
        {"label": "COIN",
         "pattern": [{"LEMMA": "kwartnik"}],
         "id": "polgrosz"
        },
        {"label": "COIN",
         "pattern": [{"TEXT": "półgr"}],
         "id": "polgrosz"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"szer"}, {"IS_PUNCT":True}, {"TEXT": "półgr"}],
         "id": "polgrosz"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"szer"}, {"IS_PUNCT":True}, {"LEMMA": "kwartnik"}],
         "id": "polgrosz"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA":"wielki"}, {"LEMMA": "kwartnik"}],
         "id": "polgrosz"
        },
        # skojec
        {"label": "COIN",
         "pattern": [{"TEXT":"sk"}, {"IS_PUNCT":True}],
         "id": "skojec"
        },
        # skojec_groszy
        {"label": "COIN",
         "pattern": [{"TEXT":"sk"}, {"IS_PUNCT":True}, {"TEXT":"gr"}],
         "id": "skojec_groszy"
        },
        # skojec_groszy_czeskich
        {"label": "COIN",
         "pattern": [{"TEXT":"sk"}, {"IS_PUNCT":True}, {"TEXT":"gr"}, {"TEXT":"czes"},
                     {"IS_PUNCT":True}],
         "id": "skojec_groszy_czeskich"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"sk"}, {"IS_PUNCT":True}, {"TEXT":"gr"}, {"LEMMA":"czeski"}],
         "id": "skojec_groszy_czeskich"
        },
        # skojec_groszy_monety_polskiej
        {"label": "COIN",
         "pattern": [{"TEXT":"sk"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"TEXT":"krak"},
                     {"IS_PUNCT":True}],
         "id": "skojec_groszy_monety_polskiej"
        },
        {"label": "COIN",
         "pattern": [{"TEXT":"sk"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"},
                     {"LEMMA":{"IN":["obiegowy","pospolity"]}}],
         "id": "skojec_groszy_monety_polskiej"
        },
        # solid
        {"label": "COIN",
         "pattern": [{"LEMMA":"solid"}],
         "id": "solid"
        },
        # szeląg
        {"label": "COIN",
         "pattern": [{"LOWER":"sz"}, {"IS_PUNCT":True}],
         "id": "szeląg"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA":{"IN":["szeląg", "szyling"]}}],
         "id": "szeląg"
        },
        # szelag_litewski
        {"label": "COIN",
         "pattern": [{"LEMMA":"szeląg"}, {"TEXT":"lit"}, {"IS_PUNCT":True}],
         "id": "szeląg"
        },
        # ternar
        {"label": "COIN",
         "pattern": [{"LEMMA":"ternar"}],
         "id": "ternar"
        },
        {"label": "COIN",
         "pattern": [{"LEMMA":"mały"}, {"LEMMA":"kwartnik"}],
         "id": "ternar"
        },
        # wiardunek
        {"label": "COIN",
         "pattern": [{"TEXT":"wiard"}, {"IS_PUNCT":True}],
         "id": "wiardunek"
        },
        # wiardunek_groszy_monety_polskiej
        {"label": "COIN",
         "pattern": [{"TEXT":"wiard"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"},
                     {"LEMMA":{"IN":["obiegowy","pospolity"]}}],
         "id": "wiardunek_groszy_monety_polskiej"
        },
        # wiardunek_monety_chelminskiej
        {"label": "COIN",
         "pattern": [{"TEXT":"wiard"}, {"IS_PUNCT":True}, {"TEXT":"chełm"},{"IS_PUNCT":True},
                     {"LEMMA":"moneta"}],
         "id": "wiardunek_monety_chelminskiej"
        },
        # wiardunek_monety_torunskiej
        {"label": "COIN",
         "pattern": [{"TEXT":"wiard"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"TEXT":"tor"},
                     {"IS_PUNCT":True}],
         "id": "wiardunek_monety_torunskiej"
        },
        # wiardunek_polgroszy
        {"label": "COIN",
         "pattern": [{"TEXT":"wiard"}, {"IS_PUNCT":True}, {"TEXT":"w"}, {"TEXT":"półgr"}],
         "id": "wiardunek_polgroszy"
        }
    ]
    return patterns
