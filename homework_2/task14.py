# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
number = int(input('Введите число N: '))
grade = 0
while 2 ** grade <= number:
    print(2 ** grade)
    grade +=1