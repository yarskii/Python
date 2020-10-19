with open('text_task2.txt', 'r') as obj:
    lines = 0
    num = 1
    for i in obj:
        flag = i.split()
        word = len(flag)
        if len(flag) == 0:
            print(f'Строка {num} пустая')
            num += 1
            continue
        print(f'Количество слов в строке {num}: {word}')
        num += 1
        if i.strip():
            lines += 1

    print(f'Количество строк с информацией: {lines}')

