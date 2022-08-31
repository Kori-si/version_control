# 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

list = ['123', '321', '456', '96']
count = '3'
array_find = []

for find_count in list:
    if count in find_count:
        array_find.append(find_count)
print(array_find)