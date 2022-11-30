# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101
# 3 -> 11
# 2 -> 10
number = int(input("Type a number: "))
n_double = ""
while number != 0:
    n_double = str(number%2) + n_double
    number //=2
print(n_double)