# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

lst = []
for i in range(0, 20):
    lst.append(randint(0, 10))
print('Первый массив ', lst)  # Список из рандомных чисел

more_often_num = 0
for i in lst:
    if lst.count(more_often_num) < lst.count(i):
        more_often_num = lst.index(i)
print('В данном массиве число ', more_often_num, 'встречается чаще других - ', lst.count(more_often_num), 'шт.')
