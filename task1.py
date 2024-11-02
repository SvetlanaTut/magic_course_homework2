# Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# 1 задание, 1 часть.

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
stroka = "qwe"

count = 0
position = -1

for i in range(len(my_list)):
    if my_list[i] == stroka:
        count += 1
        if count == 2:
            position = i
            break

if position != -1:    
    print("Позиция второго вхождения:", position)
else: 
    print("Второго вхождения нет")

# Задание 1, часть 2

my_list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
stroka1 = "йцу"

count1 = 0
position2 = -1

for i in range(len(my_list1)):
    if my_list1[i] == stroka1:
        count1 += 1
        if count1 == 2:
            position1 = i
            break
if position1 != -1:    
    print("Позиция второго вхождения:", position1)
else: 
    print("Второго вхождения нет")  

# Задание 1, 3 часть

my_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
stroka2 = "йцу"

count2 = 0
position2 = -1

for i in range(len(my_list2)):
    if my_list2[i] == stroka2:
        count2 += 1
    if count2 == 2:
        position2 = i
        break
if position2 != -1:
    print("Позиция второго вхождения:", position2)
else:
    print("Второго вхождения нет", position2)

# Задание 1,  часть 4

my_list3 = ["123", "234", 123, "567"]
stroka3 = "123"

count3 = 0
position3 = -1

for i in range(len(my_list3)):
    if my_list3[i] == 0:
        count3 += 1
    if count3 == 2:
        position3 = i
        break

if position3 != -1:
    print("Позиция второго вхождения:", position3)
else:
    print("Второго вхождения нет", position3)
    