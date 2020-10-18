x = float(input('Введите действительное положительное число x'))
y = int(input('Введите целое отрицательное число y'))

def power(x, y):
    operation = x ** y
    return operation

answer = round(power(x, y), 3)
print(answer)
