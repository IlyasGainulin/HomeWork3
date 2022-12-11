# Просмотреть свои предыдущие ДЗ и попробовать применить к ним 
# lambda, filter, map, zip, enumerate, list comprehension, там где это возможно.
# Формат сдачи: создаем новый репозиторий, в первую часть (закомментированную) 
# вставляем изначальную версию задания, во вторую с изменениями. 
# Отправляем так же ссылкой два-три примера, желательно с разными примерами 
# (lambda, filter, map, zip, enumerate, list comprehension)


# 1.3.Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int (input('Введите число:'))
t = True
f = False
if ((n % 5 == 0) and (n % 10 == 0)) or (n / 15 == 0) and (n / 30 == 0):
    print(t)
else:
    print(f)


# ВЫПОЛНЕНИЕ ЧЕРЕЗ lambda:

# n = int (input('Введите число:'))
# num = lambda n: n % 5 == 0 and n % 10 == 0 or n % 15 == 0 not in n % 30 == 0
# result = num(n)
# print(result)


# 2.3.Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.

# 1 способ
# print('Программа задает список из n чисел последовательности (1+ 1/n)^n и выведит на экран их сумму')
# n = int(input('Введите число N:'))
# pos = [round((1+1/i)**i, 2) for i in range(1, n + 1)]
# print(f'Последовательность:{pos}\nСумма чисел: {round(sum(pos), 2)}')


# 2 способ
# import math

# a = int(input('Введите число:'))

# def array(n):
#     listA = []
#     buf = 1
#     for i in range (1, n+1):
#         listA.append((1+1/i)**i)
#         #buf*=i
#     return listA

# print(array(a))
# print(sum(array(a)))


# ВЫПОЛНЕНИЕ ЧЕРЕЗ list:

# n =int(input('Введите число N:'))
# res = list(range(1, n+1))
# print(list(map(lambda x: (1+1/x)**x, res)))