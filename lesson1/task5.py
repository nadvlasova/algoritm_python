# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# алгоритм решения:
# 1. Заводим переменные для ввода букв.
# 2. Вычисляем позицию в алфавите для каждой из букв.
# 3. высчитываем количество букв находящихся между.

a = ord(input())
b = ord(input())
a = a - ord('a') + 1
print('Позиция первой буквы:', a)
b = b - ord('a') + 1
print('Позиция второй буквы:', b)
c = abs(a-b) - 1
print('Между этими буквами', c, 'символов')
