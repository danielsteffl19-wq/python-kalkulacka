from pathlib import Path


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


def nacti_historii():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as soubor:
            return [radek.strip() for radek in soubor]
    except FileNotFoundError:
        return []


def uloz_vypocet(vypocet):
    with open(HISTORY_FILE, "a", encoding="utf-8") as soubor:
        soubor.write(vypocet + "\n")


historie = nacti_historii()


while True:
    try:
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
    except ValueError:
        print("Neplatné číslo! Zkus to znovu.")
        continue

    operace = input(
        "Zadej operaci (+, -, *, /, :) "
        "nebo (h pro historii, q pro ukončení): "
    )

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
                print()

        case "+":
            vysledek = secti(a, b)
            vypocet = f"{a} + {b} = {vysledek}"
            print("Výsledek:", vysledek)
            historie.append(vypocet)
            uloz_vypocet(vypocet)

        case "-":
            vysledek = odecti(a, b)
            vypocet = f"{a} - {b} = {vysledek}"
            print("Výsledek:", vysledek)
            historie.append(vypocet)
            uloz_vypocet(vypocet)

        case "*":
            vysledek = vynasob(a, b)
            vypocet = f"{a} * {b} = {vysledek}"
            print("Výsledek:", vysledek)
            historie.append(vypocet)
            uloz_vypocet(vypocet)

        case "/" | ":":
            vysledek = vydel(a, b)

            if vysledek is None:
                print("Nelze dělit nulou!")
            else:
                vypocet = f"{a} / {b} = {vysledek}"
                print("Výsledek:", vysledek)
                historie.append(vypocet)
                uloz_vypocet(vypocet)

        case _:
            print("Neplatná operace!")