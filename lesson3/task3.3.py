# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

from random import randint

lst = []
for i in range(0, 10):
    lst.append(randint(0, 99))
print('Массив до изменения ', lst)  # Список из рандомных чисел

mx = lst[0]
mn = lst[0]

for i in lst:
    if i > mx:
        mx = i
    elif i < mn:
        mn = i
mn_index = lst.index(mn)
mx_index = lst.index(mx)

lst[mn_index], lst[mx_index] = lst[mx_index], lst[mn_index]

print('Массив после перестановки минимального и максимального чисел ', lst)
