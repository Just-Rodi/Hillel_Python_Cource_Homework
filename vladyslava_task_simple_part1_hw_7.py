"""
Начинающий уровень:
Для начала в одном файле.
1) 5 примеров list comprehension
2) 5 examples with DICT comprehension
3) 5 примеров с set comprehensions
"""
one_list: list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
two_list: list = ['green', 'yellow', 'white', 'red']
three_list: list = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
four_list: list = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
                   'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 1) 5 примеров list comprehension
list_1: list = [i for i in range(9)]
list_2: list = [i ** i for i in range(9, 2, -1)]
list_3: list = [i for i in three_list[::-1]]
list_4: list = [i.upper() for i in three_list]
list_5: list = [i[::-1] for i in three_list]
print(list_1, list_2, list_3, list_4, list_5, sep="\n")

# 2) 5 examples with DICT comprehension
dict_1: dict = {i: "method_list" for i in three_list}
dict_2: dict = {i: i ** i for i in range(10)}
dict_3: dict = {i.upper(): i.lower() for i in three_list if isinstance(i, str)}
dict_4: dict = {i: 'None' for i in three_list}
dict_5: dict = {i: [j for j in two_list] for i in three_list}
print(dict_1, dict_2, dict_3, dict_4, dict_5, sep='\n')

# 3) 5 примеров с set comprehensions
set_1: set = {i for i in one_list}
set_2: set = {i for i in four_list}
set_3: set = {i * 2 for i in one_list}
set_4: set = {i.upper() for i in four_list}
set_5: set = {one_list[i] for i in range(len(one_list))}
print(set_1, set_2, set_3, set_4, set_5, sep="\n")
