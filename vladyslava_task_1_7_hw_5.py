"""
Задача 1. 10 баллов
пользователь вводит пароль первый раз система запоминает и просит повторить пароль проверяет его если нет то просит
повторить. А если совпал то сообщение.
"""

pass_input: str = input('Enter your password:\t')
while True:
    if pass_input == input('Enter your password again:\t'):
        print('Your password is correct')
        break
    else:
        continue

"""
Задача_2. 5 баллов
Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.
Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
Результат: ['bear', 'milk']
"""
product_list: list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
print(product_list)
del_product: str = input('Fill up product for delete: ')
while True:
    if del_product in product_list:
        product_list.remove(del_product)
    else:
        print(f'{product_list}\n')
        break

"""
Задача_3. 10 баллов
Тема while and else
дан список произвольный с int нужно вывести "all numbers are even" если все четные и NO если нет
"""
numbers_list: list = [24, 24, 64, 44, 75, 530]
# доп. лист для проверки четных [12, 22, 66, 44, 76, 534]
number: int = 0
for i in numbers_list:
    if i % 2 != 0:
        print("NO\n")
        break
    else:
        number += 1
if number == len(numbers_list):
    print("All numbers are even\n")

"""
Задача_4 25 баллов
написать программу которая будет создавать список методов из доступных методов питон объектов. 
Под доступными подразумевается методы без подчеркиваний. Функции dir()
т.е для объекта set должен быть список методов
['add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'isdisjoint', 'issubset','issuperset', 'pop',
'remove','union', 'update']
"""
ex_set_list: list = (dir(set))
methods_list: list = []
for i in ex_set_list:
    for j in i:
        if j.isalpha():
            methods_list.append(i)
            break
        else:
            break
print(methods_list)

"""
Задача_6 5 балов
Написать примеры всех методов из set объекта.
Пример:
set1 = {1,2,3}
# add
set1.add(4)
# update
set1.update([2,3,4,5])
"""

set_1 = {1, 2, 3}
set_2 = {2, 4, 6}

# clear - удаляет все объекты в сете
set_1.clear()

# add - добавляет один элемент
set_1.add(4)

# update - добавляет перечень объектов
set_2.update([1, 2, 3, 4, 5, 6])
set_1.update([5, 6, 7, 8, 9, 10])
set_1 |= set_2

# discard - удаляет элемент если его значение присутствует в сете
set_2.discard(6)

# remove - удаляет элемент если его значение присутствует в сете
set_2.remove(2)

# pop - удаляет случайный элемент сета, удалённому присваивается новая переменная
a = set_2.pop()

# intersection - позволяет найти пересечение множества с одной или более последовательностями
set_1.intersection(set_2)
sec = set_1 & set_2
set_1 &= set_2

# union - объединение множеств
set_1.union(set_2)
un = set_1 | set_2

# difference - позволяет получить элементы множества, которых нет в одной или более последовательности
set_1.difference(set_2)
dif = set_1 - set_2

# copy - делает копию
copy_set1 = set_1.copy()

# isdisjoint - возвращает TRUE, если общих элементов нет
set_1.isdisjoint(set_2)

# issubset - возвращает TRUE , если set_1 полностью лежит в set_2
set_1.issubset(set_2)
s_s1: bool = set_1 <= set_2
s_s2: bool = set_1 < set_2

# issuperset - возвращает TRUE , если set_2 полностью лежит у set_1
set_1.issuperset(set_2)
s_s3: bool = set_1 >= set_2
s_s4: bool = set_1 > set_2

"""
Задача_7 25 баллов
Тема frozenset.
Создать frozenset (Прочитать что это где вам удобно).
Необходимо посчитать длину этой коллекции(frozenset) без помощи функции len().
И вывести ее в косноль.
"""

fro_set: frozenset = frozenset(dir(frozenset))
fro_set_int: int = 0
for i in fro_set:
    fro_set_int += 1
print(fro_set_int)
