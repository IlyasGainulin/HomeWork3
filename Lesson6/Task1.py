#Задача: предложить улучшения кода для уже решённых задач:
#С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
#(выбрать 3 любые)

# 2.3.Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.

print('Программа задает список из n чисел последовательности (1+ 1/n)^n и выведит на экран их сумму')
n = int(input('Введите число N:'))
pos = [round((1+1/i)**i, 2) for i in range(1, n + 1)]
print(f'Последовательность:{pos}\nСумма чисел: {round(sum(pos), 2)}')


# Решение

#n =int(input('Введите число N:'))
#res = list(range(1, n+1))
#print(list(map(lambda x: (1+1/x)**x, res)))


#3.1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#*Пример:*
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sumOddIndex(list1):
    sum = 0
    for i in range(len(list1)):
        if i % 2 != 0:
            sum += list1[i]
    print(f"Сумма элементов на нечетных позициях = {sum}")

list1 = [2, 3, 5, 9, 3]
sumOddIndex(list1)
list1 = list(map(int, input("Введите числа через пробел:\n").split()))
sumOddIndex(list1)


# Решение
#lst = [2,3,5,9,3] 
#lst = list(map(int, input('Введите числа через пробел: ').split())) 
#def summaOdd(lst): 
#    countSum = 0 
#    for i in range(len(lst)): 
#        if i%2 != 0: 
#            countSum+=lst[i] 
#    print(countSum) 
#summaOdd(lst)
