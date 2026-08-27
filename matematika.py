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
        return None
    return a / b


def cele_deleni(a, b):
    if b == 0:
        return None
    return a // b


def zbytek(a, b):
    if b == 0:
        return None
    return a % b


def mocnina(a, b):
    try:
        return math.pow(a, b)
    except ValueError:
        return None

def odmocnina(a):
    if a < 0:
        return None

    return math.sqrt(a)

def faktorial(a):
    if a < 0 or not a.is_integer():
        return None

    return math.factorial(int(a))

def absolutni_hodnota(a):
    return abs(a)