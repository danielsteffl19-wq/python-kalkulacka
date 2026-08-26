from pathlib import Path


HISTORY_FILE = Path(__file__).parent / "history.txt"


# ---- Načtení historie ----

def nacti_historii():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as soubor:
            return [radek.strip() for radek in soubor]
    except FileNotFoundError:
        return []


# ---- Uložení výpočtu ----

def uloz_vypocet(vypocet):
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as soubor:
            soubor.write(vypocet + "\n")
    except OSError:
        print("Historii se nepodařilo uložit.")


# ---- Zobrazení historie ----

def zobraz_historii(historie):
    if not historie:
        print("Historie je prázdná.")
        return

    print("\n=== HISTORIE ===")
    print(f"Celkem výpočtů: {len(historie)}")

    posledni_vypocty = historie[-10:]

    for cislo, vypocet in enumerate(posledni_vypocty, 1):
        print(f"{cislo}. {vypocet}")


# ---- Vyhledání v historii ----

def vyhledej_historii(historie):
    if not historie:
        print("Historie je prázdná.")
        return

    hledany_text = input(
        "Co chceš v historii vyhledat? "
    ).lower()

    nalezene = []

    for vypocet in historie:
        if hledany_text in vypocet.lower():
            nalezene.append(vypocet)

    if not nalezene:
        print("Žádný výpočet nebyl nalezen.")
        return

    print("\n=== VÝSLEDKY VYHLEDÁVÁNÍ ===")

    for vypocet in nalezene:
        print(vypocet)


# ---- Správa historie ----

def sprava_historie(historie):
    while True:
        print("\n=== HISTORIE ===")
        print("1 - Zobrazit historii")
        print("2 - Vyhledat v historii")
        print("q - Zpět")

        volba = input("Vyber možnost: ").lower()

        match volba:
            case "1":
                zobraz_historii(historie)

            case "2":
                vyhledej_historii(historie)

            case "q":
                break

            case _:
                print("Neplatná volba!")


# ---- Vymazání historie ----

def smaz_historii():
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as soubor:
            soubor.write("")
    except OSError:
        print("Historii se nepodařilo vymazat.")