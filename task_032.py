from random import randint

def ciąg_liczbowy(rozmiar, a, b):
    return [randint(a, b) for i in range(rozmiar)]

def unikalne_znaczenie(list):
    return [i for i in set(list)]

rozmiar = 10
a = 1
b = 10


origin = ciąg_liczbowy(rozmiar, a, b)

print(origin)
print(unikalne_znaczenie(origin))