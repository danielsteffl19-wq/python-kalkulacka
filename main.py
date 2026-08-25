from pathlib import Path

import math
import json


# ---- Soubory ----

BASE_DIR = Path(__file__).parent
HISTORY_FILE = BASE_DIR / "history.txt"
CONFIG_FILE = BASE_DIR / "config.json"


# ---- Matematika ----

def secti(a, b):
    return a + b


def odecti(a, b):
    return a - b


def vynasob(a, b):
    return a * b


def vydel(a, b):
    if b == 0:
        return None
    return a / b


def cele_deleni(a, b):
    if b == 0:
        return None
    return a // b


def zbytek(a, b):
    if b == 0:
        return None
    return a % b


def mocnina(a, b):
    return math.pow(a, b)


def odmocnina(a):
    if a < 0:
        return None
    return math.sqrt(a)


# ---- Historie ----

def nacti_historii():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as soubor:
            return [radek.strip() for radek in soubor]
    except FileNotFoundError:
        return []


def uloz_vypocet(vypocet):
    with open(HISTORY_FILE, "a", encoding="utf-8") as soubor:
        soubor.write(vypocet + "\n")


def zobraz_historii():
    if not historie:
        print("Historie je prázdná.")
        return

    print("\n=== HISTORIE ===")

    for vypocet in historie:
        print(vypocet)


def smaz_historii():
    global historie

    if not historie:
        print("Historie je již prázdná.")
        return

    potvrzeni = input(
        "Opravdu chceš vymazat celou historii? (a/n): "
    ).lower()

    if potvrzeni == "a":
        historie.clear()

        with open(HISTORY_FILE, "w", encoding="utf-8") as soubor:
            soubor.write("")

        print("Historie byla vymazána.")

    else:
        print("Mazání historie bylo zrušeno.")


# ---- Nastavení ----

def nacti_desetinna_mista():
    while True:
        try:
            desetinna_mista = int(
                input("Kolik desetinných míst chceš zobrazovat? ")
            )

            if desetinna_mista < 0:
                print("Počet desetinných míst nemůže být záporný.")
                continue

            return desetinna_mista

        except ValueError:
            print("Zadej celé číslo.")


def nacti_nastaveni():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as soubor:
            nastaveni = json.load(soubor)

            return nastaveni.get("desetinna_mista", 2)

    except (FileNotFoundError, json.JSONDecodeError):
        return 2


def uloz_nastaveni(desetinna_mista):
    nastaveni = {
        "desetinna_mista": desetinna_mista
    }

    with open(CONFIG_FILE, "w", encoding="utf-8") as soubor:
        json.dump(nastaveni, soubor, indent=4)


def nastaveni():
    global desetinna_mista

    print("\n=== NASTAVENÍ ===")

    print(
        f"Aktuální počet desetinných míst: "
        f"{desetinna_mista}"
    )

    desetinna_mista = nacti_desetinna_mista()

    uloz_nastaveni(desetinna_mista)

    print(
        f"Nastavení změněno na {desetinna_mista} "
        "desetinných míst."
    )


# ---- Vstup a výsledky ----

def nacti_cislo(text):
    while True:
        try:
            return float(input(text))

        except ValueError:
            print("Neplatné číslo! Zkus to znovu.")


def zaokrouhli(vysledek):
    return round(vysledek, desetinna_mista)


def zpracuj_vysledek(vypocet, vysledek):
    vysledek = zaokrouhli(vysledek)

    print("Výsledek:", vysledek)

    vypocet = f"{vypocet} = {vysledek}"

    historie.append(vypocet)

    uloz_vypocet(vypocet)


# ---- Výpočty ----

def dvojita_operace(operace, symbol):
    a = nacti_cislo("Zadej první číslo: ")
    b = nacti_cislo("Zadej druhé číslo: ")

    vysledek = operace(a, b)

    if vysledek is None:
        print("Nelze dělit nulou!")
        return

    vypocet = f"{a} {symbol} {b}"

    zpracuj_vysledek(vypocet, vysledek)


def vypocitej_mocninu():
    a = nacti_cislo("Zadej základ: ")
    b = nacti_cislo("Zadej exponent: ")

    vysledek = mocnina(a, b)

    vypocet = f"{a} ^ {b}"

    zpracuj_vysledek(vypocet, vysledek)


def vypocitej_odmocninu():
    a = nacti_cislo("Zadej číslo: ")

    vysledek = odmocnina(a)

    if vysledek is None:
        print("Nelze odmocnit záporné číslo!")
        return

    vypocet = f"√{a}"

    zpracuj_vysledek(vypocet, vysledek)


# ---- Menu ----

def zobraz_menu():
    print("\n=== KALKULAČKA ===")

    print("+   Sčítání")
    print("-   Odčítání")
    print("*   Násobení")
    print("/   Dělení")
    print("//  Celočíselné dělení")
    print("%   Zbytek po dělení")
    print("^   Mocnina")
    print("r   Odmocnina")
    print("h   Historie")
    print("c   Vymazat historii")
    print("s   Nastavení")
    print("q   Konec")


# ---- Hlavní program ----

historie = nacti_historii()
desetinna_mista = nacti_nastaveni()


while True:
    zobraz_menu()

    operace = input("Vyber operaci: ").lower()

    match operace:

        case "q":
            print("Konec programu.")
            break

        case "h":
            zobraz_historii()

        case "c":
            smaz_historii()

        case "s":
            nastaveni()

        case "+":
            dvojita_operace(secti, "+")

        case "-":
            dvojita_operace(odecti, "-")

        case "*":
            dvojita_operace(vynasob, "*")

        case "/":
            dvojita_operace(vydel, "/")

        case "//":
            dvojita_operace(cele_deleni, "//")

        case "%":
            dvojita_operace(zbytek, "%")

        case "^":
            vypocitej_mocninu()

        case "r":
            vypocitej_odmocninu()

        case _:
            print("Neplatná operace!")