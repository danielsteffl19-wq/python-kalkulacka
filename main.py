from matematika import (
    secti,
    odecti,
    vynasob,
    vydel,
    cele_deleni,
    zbytek,
    mocnina,
    odmocnina,
    faktorial,
    absolutni_hodnota
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


def zaokrouhli(vysledek, desetinna_mista):
    return round(vysledek, desetinna_mista)


def formatuj_vysledek(vysledek, desetinna_mista):
    vysledek = zaokrouhli(vysledek, desetinna_mista)

    if vysledek.is_integer():
        return int(vysledek)

    return vysledek


def zpracuj_vysledek(vypocet, vysledek, desetinna_mista, historie):
    vysledek = formatuj_vysledek(vysledek, desetinna_mista)

    print("Výsledek:", vysledek)

    vypocet = f"{vypocet} = {vysledek}"

    historie.append(vypocet)
    uloz_vypocet(vypocet)


# ---- Historie ----

def vymaz_historii(historie):
    if not historie:
        print("Historie je již prázdná.")
        return

    potvrzeni = input(
        "Opravdu chceš vymazat celou historii? (a/n): "
    ).lower()

    if potvrzeni == "a":
        historie.clear()
        smaz_historii()
        print("Historie byla vymazána.")
    else:
        print("Mazání historie bylo zrušeno.")


# ---- Nastavení ----

def nastaveni(desetinna_mista):
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

    return desetinna_mista


# ---- Výpočty ----

def dvojita_operace(operace, symbol, desetinna_mista, historie):
    a = nacti_cislo("Zadej první číslo: ")
    b = nacti_cislo("Zadej druhé číslo: ")

    vysledek = operace(a, b)

    if vysledek is None:
        print("Operaci nelze provést!")
        return

    vypocet = f"{a} {symbol} {b}"

    zpracuj_vysledek(
        vypocet,
        vysledek,
        desetinna_mista,
        historie
    )


def vypocitej_mocninu(desetinna_mista, historie):
    a = nacti_cislo("Zadej základ: ")
    b = nacti_cislo("Zadej exponent: ")

    vysledek = mocnina(a, b)

    if vysledek is None:
        print("Tuto mocninu nelze vypočítat.")
        return

    vypocet = f"{a} ^ {b}"

    zpracuj_vysledek(
        vypocet,
        vysledek,
        desetinna_mista,
        historie
    )


def vypocitej_odmocninu(desetinna_mista, historie):
    a = nacti_cislo("Zadej číslo: ")

    vysledek = odmocnina(a)

    if vysledek is None:
        print("Nelze odmocnit záporné číslo!")
        return

    vypocet = f"√{a}"

    zpracuj_vysledek(
        vypocet,
        vysledek,
        desetinna_mista,
        historie
    )

def vypocitej_faktorial(desetinna_mista, historie):
    a = nacti_cislo("Zadej číslo: ")

    vysledek = faktorial(a)

    if vysledek is None:
        print("Faktoriál lze vypočítat pouze z nezáporného celého čísla.")
        return

    vypocet = f"{a}!"

    zpracuj_vysledek(
        vypocet,
        vysledek,
        desetinna_mista,
        historie
    )

def vypocitej_absolutni_hodnotu(desetinna_mista, historie):
    a = nacti_cislo("Zadej číslo: ")

    vysledek = absolutni_hodnota(a)

    vypocet = f"|{a}|"

    zpracuj_vysledek(
        vypocet,
        vysledek,
        desetinna_mista,
        historie
    )


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
    print("!   Faktoriál")
    print("|x|  Absolutní hodnota")
    print("h   Historie")
    print("c   Vymazat historii")
    print("s   Nastavení")
    print("q   Konec")


# ---- Hlavní program ----

def main():
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
                vymaz_historii(historie)

            case "s":
                desetinna_mista = nastaveni(desetinna_mista)

            case "+":
                dvojita_operace(
                    secti,
                    "+",
                    desetinna_mista,
                    historie
                )

            case "-":
                dvojita_operace(
                    odecti,
                    "-",
                    desetinna_mista,
                    historie
                )

            case "*":
                dvojita_operace(
                    vynasob,
                    "*",
                    desetinna_mista,
                    historie
                )

            case "/":
                dvojita_operace(
                    vydel,
                    "/",
                    desetinna_mista,
                    historie
                )

            case "//":
                dvojita_operace(
                    cele_deleni,
                    "//",
                    desetinna_mista,
                    historie
                )

            case "%":
                dvojita_operace(
                    zbytek,
                    "%",
                    desetinna_mista,
                    historie
                )

            case "^":
                vypocitej_mocninu(
                    desetinna_mista,
                    historie
                )

            case "r":
                vypocitej_odmocninu(
                    desetinna_mista,
                    historie
                )
            case "!":
                vypocitej_faktorial(
                    desetinna_mista,
                    historie
                )

            case "|x|":
                vypocitej_absolutni_hodnotu(
                    desetinna_mista,
                    historie
                )

            case _:
                print("Neplatná operace!")


if __name__ == "__main__":
    main()