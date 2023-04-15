''' На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые
нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
стороной. Выведите минимальное количество монет, которые нужно перевернуть '''
import random

number_coins = int(input('введите количество монеток на столе: '))
count_heads = 0
count_tails = 0

for i in range(number_coins):
    x = random.randint(0, 1)
    print(x, end = " ")
    if x == 0:
        count_heads += 1
    else:
        count_tails += 1
if count_heads > count_tails:
    print()
    print('необходимо перевернуть: ',count_tails, 'монетки')
else:
    print()
    print('необходимо перевернуть:',count_heads, 'монетки')