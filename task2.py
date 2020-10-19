time: int = int(input('Введите время в секундах'))
while time < 0:
    print('Ошибка')
    time = int(input('Введите положительное число'))
minutes = time // 60
hour = minutes // 60
seconds = time % 60
if 0 < time < 60:
    print(f'00:00:{seconds:02}')
elif 0 < time < 3600:
    print(f'00:{minutes:02}:{seconds:02}')
else:
    if minutes >= 60:
        minutes %= 60
    print(f'{hour:02}:{minutes:02}:{seconds:02}')
