from random import randint

def ciąg_liczbowy(rozmiar, m, n):
    return [randint(m, n) for i in range(rozmiar)]

def unikalne_znaczenie(list):
    return [i for i in set(list)]

rozmiar = 25
m = 1
n = 10

origin = ciąg_liczbowy(rozmiar, m, n)
print(origin)
print(unikalne_znaczenie(origin))