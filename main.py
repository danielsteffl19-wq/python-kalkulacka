from pathlib import Path
import math


HISTORY_FILE = Path(__file__).parent / "history.txt"


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


def mocnina(a, b):
    return math.pow(a, b)


def odmocnina(a):
    if a < 0:
        return None
    return math.sqrt(a)


def nacti_historii():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as soubor:
            return [radek.strip() for radek in soubor]
    except FileNotFoundError:
        return []


def uloz_vypocet(vypocet):
    with open(HISTORY_FILE, "a", encoding="utf-8") as soubor:
        soubor.write(vypocet + "\n")


def nacti_cislo(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Neplatné číslo! Zkus to znovu.")


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


def zpracuj_vysledek(vypocet, vysledek):
    print("Výsledek:", vysledek)
    historie.append(vypocet)
    uloz_vypocet(vypocet)


def zaokrouhli(vysledek):
    return round(vysledek, desetinna_mista)


historie = nacti_historii()

desetinna_mista = 2


while True:
    print("\n=== KALKULAČKA ===")
    print("+  Sčítání")
    print("-  Odčítání")
    print("*  Násobení")
    print("/  Dělení")
    print("^  Mocnina")
    print("r  Odmocnina")
    print("h  Historie")
    print("s  Nastavení")
    print("q  Konec")

    operace = input("Vyber operaci: ").lower()

    match operace:
        case "q":
            print("Konec programu.")
            break

        case "h":
            if not historie:
                print("Historie je prázdná.")
            else:
                print("\n=== HISTORIE ===")

                for vypocet in historie:
                    print(vypocet)

        case "s":
            print("\n=== NASTAVENÍ ===")
            print(f"Aktuální počet desetinných míst: {desetinna_mista}")

            desetinna_mista = nacti_desetinna_mista()

            print(
                f"Nastavení změněno na {desetinna_mista} "
                "desetinných míst."
            )

        case "+":
            a = nacti_cislo("Zadej první číslo: ")
            b = nacti_cislo("Zadej druhé číslo: ")

            vysledek = zaokrouhli(secti(a, b))
            vypocet = f"{a} + {b} = {vysledek}"

            zpracuj_vysledek(vypocet, vysledek)

        case "-":
            a = nacti_cislo("Zadej první číslo: ")
            b = nacti_cislo("Zadej druhé číslo: ")

            vysledek = zaokrouhli(odecti(a, b))
            vypocet = f"{a} - {b} = {vysledek}"

            zpracuj_vysledek(vypocet, vysledek)

        case "*":
            a = nacti_cislo("Zadej první číslo: ")
            b = nacti_cislo("Zadej druhé číslo: ")

            vysledek = zaokrouhli(vynasob(a, b))
            vypocet = f"{a} * {b} = {vysledek}"

            zpracuj_vysledek(vypocet, vysledek)

        case "/":
            a = nacti_cislo("Zadej první číslo: ")
            b = nacti_cislo("Zadej druhé číslo: ")

            vysledek = vydel(a, b)

            if vysledek is None:
                print("Nelze dělit nulou!")
            else:
                vysledek = zaokrouhli(vysledek)
                vypocet = f"{a} / {b} = {vysledek}"

                zpracuj_vysledek(vypocet, vysledek)

        case "^":
            a = nacti_cislo("Zadej základ: ")
            b = nacti_cislo("Zadej exponent: ")

            vysledek = zaokrouhli(mocnina(a, b))
            vypocet = f"{a} ^ {b} = {vysledek}"

            zpracuj_vysledek(vypocet, vysledek)

        case "r":
            a = nacti_cislo("Zadej číslo: ")

            vysledek = odmocnina(a)

            if vysledek is None:
                print("Nelze odmocnit záporné číslo!")
            else:
                vysledek = zaokrouhli(vysledek)
                vypocet = f"√{a} = {vysledek}"

                zpracuj_vysledek(vypocet, vysledek)

        case _:
            print("Neplatná operace!")