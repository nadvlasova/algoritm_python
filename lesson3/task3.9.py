# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

h = 5
v = 5
a = []
for i in range(v):
    b = []
    for j in range(h):
        n = int(random() * 50)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = - 1
for j in range(h):
    mn = 50
    for i in range(v):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print('Максимальный среди минимальных: ', mx)
