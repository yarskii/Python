with open('text_task5.txt', 'w') as obj:
    line = input('Введите числа через пробел')
    obj.writelines(line)
    new_line = line.split()
    i = 0
    for _ in range(len(new_line)):
        i += int(new_line[_])
    obj.writelines('\n')
    obj.writelines(str(i))
    print(i)
