# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
list1 = list(map(int,input("Type numbers of the list separated by space: ").split()))
res = []
if len(list1) % 2 == 0:
    idx = len(list1)//2
else:
    idx = len(list1)//2 + 1
for i in range(0,idx): 
    res.append(list1[i] * list1[-i - 1])
print(res)