# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# list1 = [2,3,5,9,3]
list1 = list(map(int,input("Type numbers of the list separated by space: ").split()))
summ = 0
for i in range(len(list1)): 
    if (i%2) != 0:
        summ += list1[i]
print(summ)