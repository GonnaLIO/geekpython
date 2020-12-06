# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
from random import randint

list = []
y = int(input("Введите количество элементов в списке>>> "))
for i in range(0, y):
    list.append(randint(1, 5))

new_list = [el for el in list if list.count(el) < 2]
print(f"Исходный список: {list}")
print(f"Новый список список: {new_list}")