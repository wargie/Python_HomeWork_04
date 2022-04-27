from random import randint

def ciąg_liczbowy(rozmiar, a, b):
    return [randint(a, b) for i in range(rozmiar)]

def unikalne_znaczenie(list):
    return [i for i in set(list)]
a = 1
b = 20
cd = 5
d = 30
rozmiar = randint(cd, d)

origin = ciąg_liczbowy(rozmiar, a, b)
print(f'Задана последовательность чисел: {origin}')
print(f'Cписок неповторяющихся элементов исходной последовательности{unikalne_znaczenie(origin)}')