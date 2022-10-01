import os
# 1. Створіть дві змінні first=10, second=30.
#    Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
first = 10
second = 30
result = first + second
print(result)

result = second - first
print(result)

result = first * second
print(result)

result = second / first
print(result)

result = first ** second
print(result)

result = second // first
print(result)

result = second % first
print(result)

# 2. Створіть змінну і запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
#    Виведіть на екран результат кожного порівняння.

result = first > second
print(result)

result = first < second
print(result)

result = first >= second
print(result)

result = first <= second
print(result)

result = first == second
print(result)

result = first != second
print(result)

# 3. Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world".
#    Виведіть на екран.

str1 = "Hello "
str2 = "world"

result = str1 + str2
print(result)

os.system("pause")