'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
'''

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))


def sumFunction(number1, number2):
    sum = 0
    if number2 < 0:
        return 0
    sum = number1 + sumFunction(1, number2-1)
    return sum
x = sumFunction(first_number, second_number)
print(x)
