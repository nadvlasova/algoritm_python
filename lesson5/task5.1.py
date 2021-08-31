# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

enterprise = collections.namedtuple('name_enterprise', ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'year_profit'])

enterprises_count = int(input('Введите количество предприятий: '))

general_year_profit = 0



for i in range(enterprises_count):
    name_enterprise = input('Введите название предприятия: ')
    quarter_1 = int(input('Введите прибыль этого предприятия за 1-й квартал: '))
    quarter_2 = int(input('Введите прибыль этого предприятия за 2-й квартал: '))
    quarter_3 = int(input('Введите прибыль этого предприятия за 3-й квартал: '))
    quarter_4 = int(input('Введите прибыль этого предприятия за 4-й квартал: '))

    year_profit = (quarter_1 + quarter_2 + quarter_3 + quarter_4)

    general_year_profit += year_profit

    average_profit = general_year_profit / enterprises_count

    print(f'Предприятиe - {name_enterprise}, Прибыль поквартально: 1 - {quarter_1}, 2 - {quarter_2}, 3 - {quarter_3}, 4 - {quarter_4}', 'Годовой доход - {year_profit}')
    print(f'Общий годовой доход по всем компаниям - {general_year_profit}')
    print(f'Средний годовой доход по всем компаниям - {average_profit}')

    if year_profit > average_profit:
        print(f'{name_enterprise}, у этих предприятий средний годовой доход выше среднего!')
    elif year_profit < average_profit:
        print(f'{name_enterprise}, у этих предприятий средний годовой доход ниже среднего!')

# Правильные действия для вычисления выше и ниже среднего, это
# 1. Создать словарь наименование предприятия: годовой доход
# 2. Проитерироваться по значениям сравнив со средне-годовым по всем и вывести ключи.
# пока не успеваю это сделать, т.к. стараюсь тщательнее проработать тему.




