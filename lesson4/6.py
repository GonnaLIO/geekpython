# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# а)
from itertools import count

for el in count(int(input('Введите стартовое число до 20 '))):
    if el > 20:
        break
    print(el)
# б)
from itertools import cycle

my_list = [True, 'Всем привет', 666, None]
i = 1
n = int(input('Введите количество повторений>>> '))
for el in cycle(my_list):
    if i > n:
        break
    else:
        i += 1
    print(el)