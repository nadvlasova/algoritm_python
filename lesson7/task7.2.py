# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import randint
import operator

primary_array = [randint(0, 50) for i in range(20)]

print(primary_array)


def merge_sort(ar, compare=operator.lt):
    if len(ar) < 2:
        return ar[:]
    else:
        middle = int(len(ar) / 2)
        left = merge_sort(ar[:middle], compare)
        right = merge_sort(ar[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


print(merge_sort(primary_array))
