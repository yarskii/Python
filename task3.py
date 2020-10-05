n = int(input('Введите положительное число'))
while n <= 0:
    print('Ошибка')
    n = int(input('Введите положительное число'))
a = str(n)
b = a + a
c = a * 3
print(n + int(b) + int(c))
