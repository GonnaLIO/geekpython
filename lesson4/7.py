# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.

from itertools import count
from math import factorial

def fac_gen():
    for el in count(1):
        yield factorial(el)

gen = fac_gen()
n = int(input("Введите количество выводимых чисел>>> "))
x = 0
for i in gen:
    if x < n:
        print(i)
        x += 1
    else:
        break