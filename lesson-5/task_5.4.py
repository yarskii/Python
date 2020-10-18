
with open('text_task4.txt') as obj:
    translater = {'One': 'Odin', 'Two': 'Dwa', 'Three': 'Tri', 'Four': 'Chetyre'}
    russian_list = []
    for i in obj:
        i = i.split(maxsplit=1)
        russian_list.append(translater.get(i[0]) + ' ' + i[1])
    print(russian_list)

with open('text_task4_new.txt', 'w') as obj_1:
    obj_1.writelines(russian_list)
