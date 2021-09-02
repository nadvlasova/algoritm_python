# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from random import randint

primary_array = [randint(-100, 100) for i in range(20)]

print(primary_array)


def sort_bubble(ar):
    n = 1
    while n < len(ar):
        for i in range(len(ar) - n):
            if ar[i] > ar[i + 1]:
                ar[i], ar[i + 1] = ar[i + 1], ar[i]
        n += 1
    return ar


print(sort_bubble(primary_array))
