in_list = [1, 1, 2]

print(list(filter(lambda x: in_list.count(x) == 1, in_list)))
