a = float(input("Zadej první číslo: "))
b = float(input("Zadej druhé číslo: "))

operace = input("Zadej operaci (+, -, *, /): ")

match operace:
    case "+":
        print("Součet:", a + b)
    case "-":
        print("Rozdíl:", a - b)
    case "*":
        print("Součin:", a * b)
    case "/":
        print("Podíl:", a / b)
    case _:
        print("Neplatná operace!")