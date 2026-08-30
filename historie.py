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


# ---- Vymazání historie ----

def smaz_historii():
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as soubor:
            soubor.write("")
    except OSError:
        print("Historii se nepodařilo vymazat.")