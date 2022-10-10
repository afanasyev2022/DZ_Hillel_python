"""
1. Дана довільна строка.
    Напишіть код, який знайде в ній і виведе на екран кількість слів, які містять дві голосні літери підряд.
"""


dictionary = 'aaeeiioouuyyAAEEIIOOUUYY'

my_str = input('enter any words string: ')

index = dictionary.find(my_str)

print('такое количество слов с двумя гласными буквами подряд: ' [index])









"""
2. Є два довільних числа які відповідають за мінімальну і максимальну ціну. 
    Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, 
    "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988,
    "store": 37.720, "rozetka": 38.003}. 
    Напишіть код, який знайде і виведе на екран назви магазинів,
    ціни яких попадають в діапазон між мінімальною і максимальною ціною. 

Наприклад:
lower_limit = 35.9
upper_limit = 37.339
> match: "x-store", "main-service"
"""


while True:
    lower_limit = input('впишите минимальное значение: ')

    if lower_limit.isdigit():
        lower_limit = int(lower_limit)
        break
    print(f'{lower_limit} is not int number!')


while True:
    upper_limit = input('впишите максимальное значение: ')

    if upper_limit.isdigit():
        upper_limit = int(upper_limit)
        break
    print(f'{upper_limit} is not int number!')


my_dict = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003,
}


