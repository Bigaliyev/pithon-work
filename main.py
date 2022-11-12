# print("hello world")
# a = {1,2,3}
# b = {3,4,5}
# print(a | b)
# print(a & b)
#
#
# Eazy A
# a = set{10,20,30,40,50}
# b = set{30,40,50,60,70}
# print(a|b)
#
# print("hello world")
#
# a = list("hellomynameiskaira")
# print(sorted(a))
#
# b = list("12345678")
# a.sort()
# print(a)
#
#
# d = {'dict':1, 'dictionary':2}
# d = {}
#
# Eazy A
# a = int(input())
# b = int(input())
# for i in range(a,b):

# a = [5,6,7]
# for i in range(0,len(a)):
#     print(a[i],end=" ")

            # car = {
            #     "brand": "Ford",
            #     "model":"Mustang",
            #     "year": 1964
            # }
            #
            # car.pop("model")
            # print(car)

# a = ("kaira",)
# print (a)

# a = tuple("sdfadfda")
# print(a)

# An example code to take matrix input by user



# An example code to take matrix input by user


            # Eazy A
# rows = int(input("Строки: "))
# columns = int(input("Столбцы: "))
#
# matrix = []
# print("Введите значения:")
#
# for _ in range(rows):
#     vector = []
#     for _ in range(columns):
#         value = int(input())
#         vector.append(value)
#     matrix.append(vector)
# print(matrix)
#
# if len(matrix) != 0:
#     max = matrix[0][0]
#     max_col = 0
#     max_row = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if max <= matrix[i][j]:
#                 max_col = j
#                 max_row = i
#
# print(max_row,max_col)


#             M-A
# stroka = int(input("Строки: "))
# stolbes = int(input("Столбцы: "))
# sum = 0
#
# matrix = []
# print("Введите значения:")
#
# for _ in range(stroka):
#      vector = []
#      for _ in range(stolbes):
#          value = int(input())
#          vector.insert(0,value)
#      matrix.insert(0,vector)
# print(matrix)


# a = input("Как тебя зовут?:\n")
# b = input("что у тебя за имя такое дурацкое, "+ a )

from random import randint
while True:
    print("Шарик с предсказаниями!\nкаждый шарик будет выдавать случайное предсказание\nа так же может задать свой вопрос и получть ответ \n \nРежимы:\n1)Предсказание\n2)Задать вопрос")
    r = int(input())
    a ="у вас будет плохой день!"
    b = "Сегодня ваш день"
    d = "не упустите свой шанс"
    f = "сегодня ты встретишь свою судьбу"
    if r == 1:
        num = randint(1,4)
        if num == 1:
            print(a)
        elif num ==2:
            print(b)
        elif num == 3:
            print(d)
        else:
            print(f)
    elif r == 2:
        input()
        if randint(0,1) == 0:
            print("да")
        else:
            print("нет")
    flag = input("Хотели бы продолжить (да/нет)?")
    if flag != "да":
        break
