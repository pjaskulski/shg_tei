# shg_tei
Skrypty do konwersji haseł Słownika Historyczno-Geograficznego do formatu TEI

Etapy przetwarzania haseł SHG na pliki TEI XML:

- oryginalne hasła dostępne są albo w formie czystego tekstu, albo w formie HTML
- na podstawie HTML tworzony jest plik json uwzględniający strukturę hasła - podział na nagłówek i punkty (zob. [SHG](http://www.slownik.ihpan.edu.pl/search.php?id=24862))
- taki plik json jest ponownie przetwarzany, by utworzyć kolejny plik json z dokładniejszym odzwierciedleniem struktury, z podpunktami a w przypadku punktów/podpunktów zawierających tzw. regesty (zapisy zdarzeń z datą i źródełm) z podziałem na regesty i w ramach regestu z podziałem na datę, treść i źródło (bibliografię)
- przygotowany w ten sposób plik json jest gotowy do translacji na plik TEI XML. Nagłówek pliku TEI (sekcja teiHeader) jest zapisana w szablonie w dodatkowym pliku tekstowym, zawiera pola podmieniane dynamicznie np. z autorem hasła, czy listą postaci występujących w haśle. Oprócz strutury - podziału na sekcje div, p, seg zgodne ze strukturą oryginalnego hasła skrypt wykonujący translację wyszukuje również nazwy własne (NER), wykorzystując bibliotekę spaCy, model pl-nask (transformer) oraz mechanizm Entity Ruler z zestawem reguł. Osoby, miejscowości i nazwy geograficzne wyszukiwane są przez model, pozostale obiekty: nazwy urzędów miejskich, kościelnych i ziemskich, nazwy obiektów gospodarczych, fizjograficznych, monet, herbów wyszukiwane są poprzez zdefiniowane reguły. Dla osób skrypt przeprowadza także identyfikację - linkowanie (NEL) z użyciem bazy wiedzy [WikiHum](https://wikihum.lab.dariah.pl/wiki/Main_Page). 
