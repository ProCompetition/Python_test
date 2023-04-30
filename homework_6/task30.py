first_element = int(input('Введите первый элемент: '))
quantity = int(input('Введите шаг: '))
difference = int(input('Введите количество элементов: '))

for i in range(difference):
    print(first_element + i*quantity)