# Akasztófa játék

<!-- [//]: # (![Akasztófa]&#40;Hangman_OG-logo.jpg&#41;) -->
<img src="pictures/Hangman_OG-logo.jpg" alt="Hangman OG logó" width="300" height="200"><br>
<!-- <img src="pictures/Hangman_OG-logo.jpg" alt="Akasztófa logó" width="300" height="200"> -->

### Feladatok
Készítsd el az akasztófa játék alapvető működését. Használhatsz bármilyen (akár állandó) kitalálandó szót, a hangsúly a találgatás logikáján és a játék befejezésének megvalósításán van.

1. A játék célja, hogy a játékos kitalálja az összes betűt, amely a szóban szerepel.
2. A játék kezdetén az állapot így néz ki: _ _ _ _ _ _ _ _ (egy aláhúzás minden betű helyett).
3. Az állapot például így jelenik meg: _ u _ _ a _ _, ha az 'u' és az 'a' betűk ki lettek találva.
4. A játékos találgathat betűket, és ha az adott betű szerepel a szóban, akkor azok felfedésre kerülnek.
5. Ha a játékos olyan betűt találgat, ami nem szerepel a szóban, akkor elveszít egy életet.
6. Ha egy betűt már korábban kitaláltak (függetlenül attól, hogy az helyes volt-e vagy sem), akkor a játékos értesítést kap, de más nem történik.
7. Ha egy találgatás hibás (legyen az új vagy ismételt), a korábban hibásnak talált betűket a játékos láthatja.
8. A játékos akkor nyer, ha az összes betűt kitalálja a szóban.
9. A játékos akkor veszít, ha a hibás találgatások száma meghaladja az induló élet paramétert (az ismételt találgatások nem számítanak).
10. Ha a játékos a 'quit' szót gépeli be, a program elköszön és kilép.

### Kis- és nagybetű érzékenység
A játék kis- és nagybetű érzéketlen, de a megjelenítés nagybetű-érzékeny.

1. Mind a kis-, mind a nagybetűk érvényes bemenetek.
2. A kis- és nagybetűs találgatások ugyanazokat a betűket fedik fel (pl. az 'i' és 'I' egyaránt felfedi az összes 'i'-t a szóban, függetlenül attól, hogy az kis- vagy nagybetűs).
3. Az ismétlődések ellenőrzésekor a kis- és nagybetűk ugyanúgy viselkednek (pl. ha 'C' után 'c'-t adunk meg, az ismétlésnek számít).
4. A megjelenítés során azonban a betűk eredeti megjelenési formájukban láthatók (pl. ha sikeresen kitaláljuk az 'i'-t, az India esetében I _ _ i _ a lesz).

### Grafika
<img src="pictures/ascii_art.png" alt="Ascii art" width="150" height="100">
<br>
Adj hozzá ASCII grafikát az életek vizualizálásához.

1. A játék állapota egy ASCII grafikával kiegészítve jelenik meg, amely az aktuális életek számától függ.
2. A grafikai sorozat igazodik az induló élet paraméter értékéhez (minimum 3 és maximum 7 között) – ez azt jelenti, hogy a játék vége grafikája mindig ugyanaz.

### Szavak betöltése
A játék egy előre definiált szókészletből véletlenszerű szót használ.

1. A játék minden indításnál véletlenszerűen választ egy szót.
2. A játék véletlenszerűen választ egy országot a ***countries*** listából.

### Különböző szintek
<img src="pictures/difficulty_levels.jpg" alt="Nehézségi szintek" width="150" height="100"><br>
A program lehetővé teszi, hogy a játékos különböző szinteken játsszon.

1. A játék a kezdés előtt megkérdezi a játékost, hogy válasszon nehézségi szintet.
2. A szavak halmaza és az életek száma a kiválasztott szinttől függ.

#### Tipp
- A játék állapotát (például a felfedett és kimaradt betűket) tárolhatod módosítható adatszerkezetekkel (például listákkal vagy halmazokkal).
- Használj halmaz adatszerkezetet, ha olyan gyűjteményre van szükséged, amely nem tartalmazhat ismétlődő elemeket.
- Próbálj néhány (3-6) függvényt létrehozni olyan funkciókra, amelyek részben elkülöníthetők a fő folyamattól (például a bemenetek kezelésére, a megjelenítés részeire vagy a menüre). Gondolj a bemeneti követelményekre és az eredményekre ezeknél az egységeknél! Add meg a szükséges bemeneteket paraméterként, és térj vissza azzal az eredménnyel, amit a hívó oldalnak szüksége van!
- Ideális csapatméret 2 fő. Maximális csapatméret 3 fő.
