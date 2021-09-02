# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random
from random import randint

primary_array = [randint(0, 50) for i in range(21)]

print(primary_array)


def median(primary_array, k):
    if len(primary_array) == 1:
        return primary_array[0]

    pivot = random.choice(primary_array)

    left_el = [el for el in primary_array if el < pivot]
    right_el = [el for el in primary_array if el > pivot]
    pivots = [el for el in primary_array if el == pivot]

    if k < len(left_el):
        return median(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return median(right_el, k - len(left_el) - len(pivots))


print(f'Медианой массива является: \n{median(primary_array, len(primary_array) / 2)}')
primary_array.sort()
print(f'Отсортированный список: \n{primary_array}')
print(f'Медианой массива является: \n{primary_array[len(primary_array) // 2]}')
