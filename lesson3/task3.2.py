# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями
# 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

lst = []
for i in range(0, 10):
    lst.append(randint(0, 99))
print('Первый массив ', lst)  # Список из рандомных чисел

index_even = []
for i in lst:
    if i % 2 == 0:
        index_even.append(lst.index(i))
print('Второй массив ', index_even)  # Список индексов четных чисел из первого массива
