a, b = float(input('Введите делимое')), float(input('Введите делитель'))

def division(a, b):

    while b == 0:
        print('Ошибка')
        b = float(input('Введите делитель не равный 0'))
    answer = a / b
    return round(answer, 3)

print(division(a, b))
