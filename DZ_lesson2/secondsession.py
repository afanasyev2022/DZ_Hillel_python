# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
#
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
#
# - якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
#
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
#
# - якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
#
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
#
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"



age = input('Будь ласка введіть свій вік: ')
print()

if not age.isdigit():
    print('Ви ввели помилковий запис, введіть данні тільки цифрами!')

age = int(age)

if age == 17 or age == 27 or age == 37 or age == 47 or age == 57:
    print('Вам сьогодні пощастить!')

elif age == 0:
    print('Ви ввели помилковий запис, введіть данні тільки цифрами!')

elif 7 > age > 0:
    print('Де твої батьки?')

elif 16 > age >= 7:
    print('Це фільм для дорослих!')

elif 111 > age > 65:
    print('Покажіть пенсіоне посвідчення!')

elif age > 110:
    print('Або ви дуже сильний пенсіонер, або вказали не правильний вік.')

elif 65 >= age >= 16:
    print('А білетів вже немає!')

else:
    print()
