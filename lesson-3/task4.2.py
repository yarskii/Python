x = float(input('Введите действительное положительное число x'))
y = int(input('Введите целое отрицательное число y'))

def my_func(x, y):
    j = 1
    if y < 0:
        for i in range(abs(y)):
            j /= x
    if y > 0:
        for i in range(y):
            j *= x
    return j

print(round(my_func(x, y), 5))
