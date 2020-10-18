my_list = [2, 7, 4, 23, 1, 44, 44, 3, 10, 7, 4, 11]
print([my_list[i] for i in range(len(my_list)) if my_list.count(my_list[i]) == 1])
