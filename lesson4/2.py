# Представлен список чисел.
# Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
from random import randint

list = []
y = int(input("Введите количество элементов в списке>>> "))
for i in range(0, y):
    list.append(randint(1, 10))

new = [el for num, el in enumerate(list) if list[num - 1] < list[num]]
print(f"Исходный список: {list}")
print(f"Новый список список: {new}")
