# 2. Напишите программу, которая определит позицию второго вхождения строки
# в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find = "qwe"
index = -1
for i in range(len(list)):
    if(list[i] == find):
        index = i
print(index)