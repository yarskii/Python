with open('text_task1.txt', 'w') as obj:
    while True:
        line = input('Введите текст или фразу\nДля завершения ввода используйте Enter\n')
        if not line:
            break
        else:
            obj.writelines(line + '\n')
