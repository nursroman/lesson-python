#Задание 1

time = int(input('введите часы работы'))
salary = int(input('введите ставку'))
bonus = int(input('Введите премию'))
result = (time * salary) + bonus
print(f'{result}')

#Задание 2

num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_num = [el for i, el in zip(num, num[1:]) if el>i]
print(new_num)

#Задание 3

list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(list)

#Задание 4

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [el for el in numbers if numbers.count(el) == 1]
print(result)

#Задание 5

num = range(100,1001)
new_num = [el for el in num if el % 2 == 0]
print(new_num)

#Задание 6

from itertools import cycle, count
for el in count(3):
    print(el)
    if el > 9:
        break

#Задание 7

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break