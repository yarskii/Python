def my_func():
    print('Для завершения ввода используйте $')
    j = 0
    stop = 0
    while stop != 9:
        x = input('Введите числа разделенные пробелом').split()
        for i in range(len(x)):
            if x[i] == '$':
                stop = 9
                break
            float(x[i])
            j += float(x[i])
        print(f'Сумма запрашиваемых чисел = {j}')

my_func()
