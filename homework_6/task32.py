import random

generator_list = int(input('Введите размер строки: '))
list = [random.randint(0, 20)for i in range(generator_list)]
print(list)
min_number = int(input('Введите минимальное значение диапазона: '))
max_number = int(input('Введите максимальное значение диапазона: '))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)