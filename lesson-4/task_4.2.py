my_list_1 = [2, 12, 1, 3, 1, -10, 7, 1, 78, 123, 55, 100]
new_list_1 = []
[new_list_1.append(my_list_1[i + 1]) for i in range(len(my_list_1) - 1) if my_list_1[i] < my_list_1[i + 1]]

print(new_list_1)
