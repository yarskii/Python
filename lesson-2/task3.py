month = int(input('Введите месяц в виде целого числа'))
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
while month < 1 or month > 12:
    print('Ошибка')
    month = int(input())
if 2 < month < 6:
    print(season_list[1])
elif 5 < month < 9:
    print(season_list[2])
elif 8 < month < 12:
    print(season_list[3])
else:
    print(season_list[0])

