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
    return math.pow(a, b)


def odmocnina(a):
    if a < 0:
        return None
    return math.sqrt(a)