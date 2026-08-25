import json
from pathlib import Path


CONFIG_FILE = Path(__file__).parent / "config.json"


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