my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
print('Для завершения рейтинга введите - 0')
while True:
    a = int(input('Введите число'))
    if a == 0:
        break
    my_list.append(a)
    my_list.sort()
    my_list.reverse()
    print(f'Обновленный рейтинг - {my_list}')
