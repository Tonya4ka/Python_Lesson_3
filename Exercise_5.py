# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input("Type a number: "))
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
fibo_pos = list(fibonacci(n))
fibo_neg = [ (-1)**(i)*el for i,el in enumerate(fibo_pos) ][::-1]  
fibo_all = fibo_neg + [0] + fibo_pos
print(fibo_all)