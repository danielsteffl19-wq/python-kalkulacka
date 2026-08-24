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


while True:
    try:
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
    except ValueError:
        print("Neplatné číslo! Zkus to znovu.")
        continue

    operace = input(
        "Zadej operaci (+, -, *, /, :) nebo (q pro ukončení): "
    )

    match operace:
        case "q":
            print("Konec programu.")
            break

        case "+":
            print("Výsledek:", secti(a, b))

        case "-":
            print("Výsledek:", odecti(a, b))

        case "*":
            print("Výsledek:", vynasob(a, b))

        case "/" | ":":
            vysledek = vydel(a, b)

            if vysledek is None:
                print("Nelze dělit nulou!")
            else:
                print("Výsledek:", vysledek)

        case _:
            print("Neplatná operace!")