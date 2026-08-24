while True:
    try:
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
    except ValueError:
        print("Neplatné číslo! Zkus to znovu.")
        continue

    operace = input("Zadej operaci (+, -, *, /, :) nebo (q pro ukončení): ")

    match operace:
        case "q":
            print("Konec programu.")
            break

        case "+":
            print("Součet:", a + b)

        case "-":
            print("Rozdíl:", a - b)

        case "*":
            print("Součin:", a * b)

        case "/" | ":":
            if b == 0:
                print("Nelze dělit nulou!")
            else:
                print("Podíl:", a / b)

        case _:
            print("Neplatná operace!")