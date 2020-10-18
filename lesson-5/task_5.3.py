with open('text_task3.txt') as obj:
    lines = 0
    total = 0
    example = 20000
    print(f'Зарплата сотрудков больше {example} р.:')
    for i in obj:
        flag = i.split()
        salary = float(flag[1])
        total += salary
        if salary > example:
            print(i)
        lines += 1
    middle = round(total / lines, 2)
    print(f'Средня зарплата сотрудников компании: {middle} р.')
