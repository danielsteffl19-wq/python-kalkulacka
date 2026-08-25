from pathlib import Path


HISTORY_FILE = Path(__file__).parent / "history.txt"


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


def smaz_historii():
    with open(HISTORY_FILE, "w", encoding="utf-8") as soubor:
        soubor.write("")