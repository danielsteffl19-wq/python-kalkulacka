# Python kalkulačka

Jednoduchá konzolová kalkulačka vytvořená v Pythonu jako jeden z mých prvních praktických projektů.

Projekt postupně rozšiřuji o nové funkce a používám ho zároveň k procvičování Pythonu, práce se soubory, JSON, Git a GitHubu.

## Funkce

Kalkulačka aktuálně podporuje:

* ➕ sčítání
* ➖ odčítání
* ✖️ násobení
* ➗ dělení
* ^ mocninu
* √ odmocninu
* 📜 trvalou historii výpočtů
* ⚙️ nastavení počtu desetinných míst
* 💾 trvalé ukládání nastavení pomocí JSON
* 🔄 opakované výpočty bez nutnosti restartovat program
* ❌ ošetření neplatných vstupů a dělení nulou

## Použité technologie

* **Python 3**
* `math` – matematické operace
* `pathlib` – práce se soubory a cestami
* `json` – ukládání konfigurace
* Git
* GitHub
* Visual Studio Code

## Struktura projektu

```text
python-kalkulacka/
│
├── main.py              # hlavní program
├── history.txt          # historie výpočtů
├── config.json          # nastavení kalkulačky
└── README.md            # základní informace o projektu 
```

## Spuštění

Ujisti se, že máš nainstalovaný Python 3.

V terminálu přejdi do složky projektu a spusť:

```bash
python main.py
```

Případně ve Windows:

```bash
py main.py
```

## Ovládání

Po spuštění se zobrazí hlavní menu:

```text
=== KALKULAČKA ===
+  Sčítání
-  Odčítání
*  Násobení
/  Dělení
^  Mocnina
r  Odmocnina
h  Historie
s  Nastavení
q  Konec
```

### Nastavení

Pomocí `s` lze změnit počet desetinných míst.

Nastavení se uloží do:

```text
config.json
```

a při dalším spuštění se automaticky načte.

### Historie

Pomocí `h` lze zobrazit předchozí výpočty.

Historie se ukládá do:

```text
history.txt
```

## Aktuální verze

**v1.8.0 – Trvalé nastavení pomocí JSON**

### Poslední změny

* přidána konfigurace pomocí `config.json`
* nastavení počtu desetinných míst se ukládá trvale
* nastavení se automaticky načítá při spuštění programu
* zachována historie výpočtů
* zachováno zaokrouhlování výsledků

## Plánované rozšíření

Projekt budu postupně rozšiřovat. Mezi možné další funkce patří:

* mazání historie
* pokročilejší matematické operace
* převody jednotek
* lepší práce s chybami
* oddělení programu do více modulů
* testy jednotlivých funkcí
* případně grafické uživatelské rozhraní

## Dokumentace

Podrobnější popis jednotlivých funkcí a částí programu najdeš v:

**`DOCUMENTATION.md`**

## 👨‍💻 Projekt

Projekt vzniká jako praktické procvičování Pythonu a zároveň jako součást mého osobního vývoje v programování.

Postupně ho rozšiřuji a jednotlivé větší změny verzuji pomocí Git a GitHubu.
