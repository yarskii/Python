from itertools import count
print('Итерация count')
num_1 = int(input('Введите число'))
j = 0
for i in count(num_1, 1):
    if j < 10:
        print(i, end=' ')
        j += 1
    else:
        break
print()

from itertools import cycle
print('Итерация cycle')
my_list = [2, 7, 4, 23, 1, 44, 44, 3, 10, 7, 4, 11]
j = 0
for i in cycle(my_list):
    print(i, end=' ')
    j += 1
    if j > 24:
        break