# Задача 10: На столе лежат n монеток. Некоторые из них 
# лежат вверх решкой, а некоторые – гербом. Определите 
# минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же 
# стороной. Выведите минимальное количество монет, которые нужно перевернуть

coin = int(input('Колличество монеток на столе: '))
top = 0 
bot = 0
coins = []
while coin > 2:
    for i in range(coin):
        coin_side = int(input(f'введите сторону моентки 0 или 1: '))
        coins.append(coin_side)
    print(coins)
    for coin in coins:
        if coin == 0:
            top += 1
        elif coin ==1:
            bot +=1
print(top,bot)
if top > bot: 
    print(f'Победила решка!\n===============\nnНеобходимо перевернуть орлов на решку: {bot}')
else:
    print(f'Победил орел!\n===============\nНеобходимо перевернуть решек на орла: {top}')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите 
# Кате отгадать задуманные Петей числа.

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)

# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: ')) 
i=0
numbers = []
while 2 ** i <= n:
    num = (2 ** i)
    i += 1
    numbers.append(num)
print(f'Все целые степени двойки\n{numbers}\nне превосходящие {n}')
