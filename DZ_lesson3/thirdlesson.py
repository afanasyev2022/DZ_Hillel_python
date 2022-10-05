# 1.Зформуйте строку, яка містить певну інформацію про символ по його індексу в відомому слові.
# Наприклад "The [індекс символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".


while True:
    word = input('enter a word ')

    if word.isalpha():
        word = str(word)
        break
    print(f'{word} is not word!')


while True:
    index = input('enter the character number you want to find ')

    if index.isdigit():
        index = int(index)
        break
    print(f'{index} is not int number!')


while True:
    index = int(index)

    if index <= len(word):
        break
    print(f'{index} index greater than word')


symbol = word[index - 1]


print(f'The {index} symbol in {word} is {symbol} ')


# не знаю як вивести людині повідомлення про те що вона вийшла за діапазон слова



# 2.Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.



my_str = input('enter the words ')

result = len(my_str.split())

print(result)


# 3.Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.















