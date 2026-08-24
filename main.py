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


historie = []


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
            print("Výsledek:", vysledek)
            historie.append(f"{a} + {b} = {vysledek}")

        case "-":
            vysledek = odecti(a, b)
            print("Výsledek:", vysledek)
            historie.append(f"{a} - {b} = {vysledek}")

        case "*":
            vysledek = vynasob(a, b)
            print("Výsledek:", vysledek)
            historie.append(f"{a} * {b} = {vysledek}")

        case "/" | ":":
            vysledek = vydel(a, b)

            if vysledek is None:
                print("Nelze dělit nulou!")
            else:
                print("Výsledek:", vysledek)
                historie.append(f"{a} / {b} = {vysledek}")

        case _:
            print("Neplatná operace!")