# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

def find_element(a: int, b: list):
    minimum = abs(a-b[0])
    result = b[0]
    for i in range(1, len(b)):
        current = abs(a - b[i])
        if current < minimum:
            minimum = current
            result = b[i]
    return result
generator_list = int(input('Введите размер строки: '))
random_list = [random.randint(0, 25) for i in range(generator_list)]
print(f'Имеем полученный список {random_list}')
search_number = int(input('Введите число для поиска: '))
print(f'Самое ближайшее число к {search_number} в списке {find_element(search_number, random_list)}')