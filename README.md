# Kalkulačka

Jednoduchá desktopová kalkulačka vytvořená v jazyce **Python**.

Kalkulačka podporuje základní i pokročilejší matematické operace, historii výpočtů, uživatelské nastavení a ovládání pomocí klávesnice.

## Funkce

* Grafické uživatelské rozhraní pomocí Tkinter
* Sčítání, odčítání, násobení a dělení
* Celočíselné dělení a zbytek po dělení
* Mocniny a odmocniny
* Faktoriál
* Absolutní hodnota
* Logaritmus
* Historie výpočtů s možností vymazání
* Nastavení počtu desetinných míst
* Automatické ukládání historie a nastavení
* Ovládání pomocí klávesnice
* Podpora desetinné tečky i čárky
* Ošetření chyb při výpočtech

## Podporované operace

| Operace            | Symbol  |
| ------------------ | ------- |
| Sčítání            | `+`     |
| Odčítání           | `-`     |
| Násobení           | `*`     |
| Dělení             | `/`     |
| Celočíselné dělení | `//`    |
| Zbytek po dělení   | `%`     |
| Mocnina            | `^`     |
| Odmocnina          | `√`     |
| Faktoriál          | `!`     |
| Absolutní hodnota  | `\|x\|` |
| Logaritmus         | `log`   |

## Ovládání klávesnicí

Kromě tlačítek v grafickém rozhraní lze kalkulačku ovládat také pomocí klávesnice.

* `0–9` – zadávání čísel
* `+ - * / % ^` – matematické operace
* `Enter` / `=` – výpočet
* `Backspace` – smazání posledního znaku
* `C`, `Delete`, `Escape` – vymazání
* `R` – odmocnina
* `A` – absolutní hodnota
* `L` – logaritmus
* `!` – faktoriál

## Struktura projektu

```text id="g5p7bk"
kalkulacka/
├── main.py
├── matematika.py
├── historie.py
├── nastaveni.py
├── historie.txt
├── nastaveni.txt
└── README.md
```

### Moduly

* `main.py` – hlavní část aplikace a grafické rozhraní
* `matematika.py` – matematické funkce
* `historie.py` – ukládání, načítání a mazání historie
* `nastaveni.py` – ukládání a načítání nastavení

Soubory `historie.txt` a `nastaveni.txt` slouží k trvalému ukládání dat aplikace.

## Spuštění

Požadavky:

* Python 3
* Tkinter

Aplikaci lze spustit příkazem:

```bash id="v2xv4s"
python main.py
```

## Verze

Aktuální verze: **v2.0.0**

## Technologie

* Python
* Tkinter
