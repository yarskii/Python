num = int(input('Введите положительное число'))
num1 = num
maximum = num1 % 10
while num1 >= 1:
    num1 //= 10
    if num1 % 10 > maximum:
        maximum = num1 % 10
    if num1 > 9:
        continue
    else:
        print(f'Самая большая цифра в числе {num}: {maximum}')
        break
if num <= 0:
    print('Ошибка')
