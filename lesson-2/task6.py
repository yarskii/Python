print('Нажмите один любой символ для завершения')
products = input('Введите необходимы товары:\nТовар цена колличество ед.').split()
my_dict = []
my_list = []
i = 1
if len(products) == 1:
    print('Вы ничего не выбрали')
else:
    while True:
        products = input('Введите необходимы товары:\nТовар цена колличество ед.').split()
        if len(products) == 1:
            break
        my_dict = dict({
            'название': products[0],
            'цена': int(products[1]),
            'количество': int(products[2]),
            'eд': products[3]
        })
        my_list.append((i, my_dict))
        i += 1
    print(my_list)
    my_analytics = {}
    if my_list:
        for key in my_list[0][1].keys():
            my_analytics[key] = set([row[1][key] for row in my_list])
    print(my_analytics)
