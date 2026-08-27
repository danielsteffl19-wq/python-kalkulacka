import math


# ---- Matematika ----

def secti(a, b):
    return a + b


def odecti(a, b):
    return a - b


def vynasob(a, b):
    return a * b


def vydel(a, b):
    if b == 0:
        raise ValueError("Nelze dělit nulou.")

    return a / b


def cele_deleni(a, b):
    if b == 0:
        raise ValueError("Nelze dělit nulou.")

    return a // b


def zbytek(a, b):
    if b == 0:
        raise ValueError("Nelze dělit nulou.")

    return a % b


def mocnina(a, b):
    try:
        return math.pow(a, b)
    except ValueError:
        raise ValueError(
            "Tuto mocninu nelze vypočítat."
        )


def odmocnina(a):
    if a < 0:
        raise ValueError(
            "Nelze odmocnit záporné číslo."
        )

    return math.sqrt(a)


def faktorial(a):
    if a < 0 or not a.is_integer():
        raise ValueError(
            "Faktoriál lze vypočítat pouze z nezáporného celého čísla."
        )

    return math.factorial(int(a))


def absolutni_hodnota(a):
    return abs(a)


def logaritmus(a, zaklad):
    if a <= 0 or zaklad <= 0 or zaklad == 1:
        raise ValueError(
            "Logaritmus nelze pro zadané hodnoty vypočítat."
        )

    return math.log(a, zaklad)