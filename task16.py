import random

size_of_range = int(input('Введите количество чисел: '))

ranges = [random.randint(0, 20) for i in range(size_of_range)]
# print(*ranges)
number = int(input('Введите число для поиска: '))
count = 0
for i in range(0, size_of_range):
    if ranges[i] == number:
        count +=1
print(f'В составленном списке {ranges} запрошенное число {number} встречается {count} раз')