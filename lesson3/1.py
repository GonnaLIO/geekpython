# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(*args):

    try:
        arg1 = int(input("Введите первое число>>> "))
        arg2 = int(input("Введите второе число>>> "))
        res = arg1 / arg2
    except ValueError:
        return 'Неверное значение, введите число'
    except ZeroDivisionError:
        return "Ошибка! На ноль делить нельзя!"

    return res

print(f'Ответ:  {div()}')