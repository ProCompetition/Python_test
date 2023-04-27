'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
целую степень B с помощью рекурсии.
'''

base = int(input('Введите число: '))
power = int(input('Введите степень: '))

def composition_power(number, power_level):
    sum = 0
    if power_level < 1:
        return 1
    sum = number * composition_power(number, power_level-1)
    return sum
composition = composition_power(base, power)
print(composition)