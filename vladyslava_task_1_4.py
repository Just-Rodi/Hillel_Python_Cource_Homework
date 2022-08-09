"""
Task1. 5 points
Написать функцию, которая будет принимать 3 аргумента (int) и находить максимум из них
"""


def max_value1(one, two, three):
    return max(one, two, three)


print(max_value1(1, 9, 24))

"""
Task2. 10 points
Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
Затем используя функцию1 (вызвать ее) написать функцию2 которая будет принимать 3 аргумента и находить максимум с 
помощью функции1.
в итоге будет .
псевдокод
функция_нахождения_макс_из_2х(арг1, арг2):
return максимальное значение из 2х аргументов
функция_нахождения_макс_из_3х(арг1, арг2, арг3):
использую тут функция_нахождения_макс_из_2х()
return максимальное значение из 3х аргументов.
"""


def max_value2(one: int, two: int) -> int:
    return max(one, two)


def max_value3(one: int, two: int, three: int) -> int:
    return max(max_value2(one, two), three)


print(max_value3(6, 9, 12))

"""
Task 3. 10 points Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.
Пример(Example)
Input: [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
Otput: [('cola', 1), ('milk', 2), ('bread', 5), ('eggs', 30)]
"""

ex_list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
ex_list2 = dict(ex_list)
ex_list2 = sorted(ex_list2.items(), key=lambda i: i[1])
print(ex_list2)

"""
Task 4. 30 points познакомиться с модулем datetime и написать программу с помощью lambda для возвращение текущего года, 
месяца , дня
например результат должен быть таким
import datetime
now = datetime.datetime.now()
.....ваш код))
print(year(now))
print(month(now))
print(day(now))
скинуть мне ссылку на документациюю по datetime.
"""

import datetime

now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()

print(year(now))
print(month(now))
print(day(now))
print(t(now))

"""
Ссылка на документацию по datetime. https://docs.python.org/3/library/datetime.html?highlight=datetim
"""
