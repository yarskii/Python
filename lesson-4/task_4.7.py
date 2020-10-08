n = int(input('Введите число для расчета факториала'))
def fact(n):
    factorial = 1
    if n == 0:
        print(1)
    for i in range(1, n+1):
        factorial *= i
        yield factorial
        n -= 1

for el in fact(n):
    print(el)
