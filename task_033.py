from random import randint
k = 5
a = randint(0, 101)
b = randint(0, 101)
print(f'{a}*x^{k} + {b}*x + 5 = 0')
with open('task_033.txt', 'w') as data:
    data.write(f'{a}*x^{k} + {b}*x + 5 = 0')