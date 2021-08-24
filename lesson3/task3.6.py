# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

lst = []
for i in range(0, 10):
    lst.append(randint(0, 99))
print('Первый массив ', lst)  # Список из рандомных чисел

mx = lst[0]
mn = lst[0]

for i in lst:  # выясняем минимальное и максимальное число
    if i > mx:
        mx = i
    elif i < mn:
        mn = i

mn_index = lst.index(mn)  # выясняем индексы минимального и максимального чисел в массиве
mx_index = lst.index(mx)


if mn_index > mx_index:  # если минимальное число стоит после максимального,
    mn_index, mx_index = mx_index, mn_index  # меняем их местами, чтобы получить интервал для итерации

summa = 0
for i in range(mn_index +1, mx_index):
    summa += lst[i]
print(summa)

