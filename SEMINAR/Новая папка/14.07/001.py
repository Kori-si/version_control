# list() - список: изменяемый, индексируемый
# tuple() - кортеж: неизменяемый, индексируемый
# set() - множество: изменяемый, неиндексируемый
# dict() - словарь: изменяемый, индексируемый по ключу

# 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.


str_list = ['hbg2u3g54', '34', 'jk90']

s_nym = input('Enter the number: ')
is_found = False

for i in str_list:
    print(i)
    if i in (s_nym):
        is_found = True
        break
print(is_found)


# def findNumber(num: int, strr: list):
# num = str(num)
# for i in range(len(strr)):
# helpForList = strr[i]
# index = helpForList.find(num)
# if index > -1:
# return 'Number присутствует.'
# return 'Number отсутсвует'



# listStrings = ['123','231','345','453','523']
# NumberN = Input_values('Enter number: ')
# print(findNumber(NumberN, listStrings))
