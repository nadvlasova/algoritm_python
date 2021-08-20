# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random
a = random.randint(0, 100)
print('Угадайте загаданное число с 10 попыток.')
attempt = 1
while attempt <= 10:
    b = int(input('Попытка номер: ' + str(attempt) + ' - '))
    if b > a:
        print('Ваше число больше загаданного, попробуйте число по-меньше!')
    elif b < a:
        print('Ваше число меньше загаданного, попробуйте число по-больше!')
    else:
        print('Вы угадали с %d-й попытки' % attempt)
        break
    attempt += 1
else:
    print('Попытки закончились! Вы проиграли!')
