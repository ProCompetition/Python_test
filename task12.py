'''Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.'''

sum = int(input('Введите сумму чисел: '))
composition = int(input('Введите произведение чисел: '))

for first_number in range(sum):
    for second_number in range(composition):
        if first_number + second_number == sum and first_number * second_number == composition:
            print('Загаданные числа это:',first_number, 'и' ,second_number)

