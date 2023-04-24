import random

print('Я загадал какое то число от 1 до 20.')
print('Давайте ты попробуешь его угадать за 5 попыток?')

random_number = random.randint(1, 20)

guesses_made = 0

while guesses_made < 5:
    your_number = int(input('Как думаете, какое число я загадал? Твое число: '))
    guesses_made +=1
    if random_number > your_number:
        print('Мое число больше')
    elif random_number < your_number:
        print('Мое число меньше')
    elif random_number == your_number:
        break
if your_number == random_number:
    print(f'Ты выиграл')
else:
    print(f'Ты проиграл я загадал {random_number}')





'''
if your_number > random_number:
    print('Мое число не такое большое, попробуй еще раз')
elif your_number < random_number:
    print('Мое число немного больше чем ты думаешь, попробуй еще раз')
else:
    print('Ура, ты угадал :) ')
    '''



