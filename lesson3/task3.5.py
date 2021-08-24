# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

lst = []
for i in range(0, 10):
    lst.append(randint(-99, 99))
print('Первый массив ', lst)  # Список из рандомных чисел

max_negative_num = 0

for i in lst:
    if lst[max_negative_num] > i:
        max_negative_num = lst.index(i)
print(max_negative_num)
