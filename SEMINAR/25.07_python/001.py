# [1, 1, 2] -> [2]
my_list = [1, 1, 2]

m = [x for x in my_list if my_list.count(x) < 2]

print(m)
