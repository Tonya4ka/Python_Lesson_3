# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list1 = list(map(float,input("Type numbers of the list separated by space: ").split()))
list2 = [round(i%1,2) for i in list1 if i%1 != 0]
print(max(list2) - min(list2))