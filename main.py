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


historie = nacti_historii()


while True:
    print("\n=== KALKULAČKA ===")
    print("+  Sčítání")
    print("-  Odčítání")
    print("*  Násobení")
    print("/  Dělení")
    print("^  Mocnina")
    print("r  Odmocnina")
    print("h  Historie")
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

        case "+":
            a = nacti_cislo("Zadej první číslo: ")
            b = nacti_cislo("Zadej druhé číslo: ")

            vysledek = secti(a, b)
            vypocet = f"{a} + {b} = {vysledek}"

            print("Výsledek:", vysledek)

            historie.append(vypocet)
            uloz_vypocet(vypocet)

        case "-":
            a = nacti_cislo("Zadej první číslo: ")
            b = nacti_cislo("Zadej druhé číslo: ")

            vysledek = odecti(a, b)
            vypocet = f"{a} - {b} = {vysledek}"

            print("Výsledek:", vysledek)

            historie.append(vypocet)
            uloz_vypocet(vypocet)

        case "*":
            a = nacti_cislo("Zadej první číslo: ")
            b = nacti_cislo("Zadej druhé číslo: ")

            vysledek = vynasob(a, b)
            vypocet = f"{a} * {b} = {vysledek}"

            print("Výsledek:", vysledek)

            historie.append(vypocet)
            uloz_vypocet(vypocet)

        case "/":
            a = nacti_cislo("Zadej první číslo: ")
            b = nacti_cislo("Zadej druhé číslo: ")

            vysledek = vydel(a, b)

            if vysledek is None:
                print("Nelze dělit nulou!")
            else:
                vypocet = f"{a} / {b} = {vysledek}"

                print("Výsledek:", vysledek)

                historie.append(vypocet)
                uloz_vypocet(vypocet)

        case "^":
            a = nacti_cislo("Zadej základ: ")
            b = nacti_cislo("Zadej exponent: ")

            vysledek = mocnina(a, b)
            vypocet = f"{a} ^ {b} = {vysledek}"

            print("Výsledek:", vysledek)

            historie.append(vypocet)
            uloz_vypocet(vypocet)

        case "r":
            a = nacti_cislo("Zadej číslo: ")

            vysledek = odmocnina(a)

            if vysledek is None:
                print("Nelze odmocnit záporné číslo!")
            else:
                vypocet = f"√{a} = {vysledek}"

                print("Výsledek:", vysledek)

                historie.append(vypocet)
                uloz_vypocet(vypocet)

        case _:
            print("Neplatná operace!")