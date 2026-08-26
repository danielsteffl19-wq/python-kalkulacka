from matematika import (
    secti,
    odecti,
    vynasob,
    vydel,
    cele_deleni,
    zbytek,
    mocnina,
    odmocnina
)

from historie import (
    nacti_historii,
    uloz_vypocet,
    sprava_historie,
    smaz_historii
)

from nastaveni import (
    nacti_desetinna_mista,
    nacti_nastaveni,
    uloz_nastaveni
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


# ---- Nastavení ----

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
            sprava_historie(historie)

        case "c":
            smaz_historii()
            historie = nacti_historii()

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