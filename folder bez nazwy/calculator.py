import math


def dod(x, y):
    return x + y


def ode(x, y):
    return x - y


def mno(x, y):
    return x * y


def dziel(x, y):
    if y == 0:
        raise Exception("nie przez zero");
    return x / y


def pot(x):
    return x * x


def pierw(x):
    return math.sqrt(x)


def proc(x, y):
    return 100 * float(x) / float(y)
