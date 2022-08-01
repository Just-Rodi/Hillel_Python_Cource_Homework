"""
Task 1. 5 points
сложить словари в один.
использовать for и dict methods.
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
"""
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}

one_list_dicts = [first, second, third, fourth, fifth]
dict_unit = {}
for list_dict in one_list_dicts:
    dict_unit.update(one_list_dicts)
print(dict_unit)

"""
Task 2. 10 points
1. Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей
Пример:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15:
225}
2. просуммировать все значения(values), делается в одну строку.(look build in functions)
"""
example_dict = {}
for i in range(11, 21):
    example_dict.setdefault(i, i ** 2)
print(example_dict)
print(sum(example_dict.values()))

"""
Task3. 5 points
отсортировать словарь по ключам
"""
big_animals = {'Elephant': 'Слон', 'Giraffe': 'Жираф', 'Unicorn': 'Единорог'}
small_animals = {'Mouse': 'Мышь', 'Snake': 'Змея', 'Kitty': 'Котёнок'}
water_animals = {'Dolphin': 'Дельфин', 'Whale': 'Кит', 'Fish': 'Рыба'}

one_list_animals = [big_animals, small_animals, water_animals]
dictionary_unit = {}
for one_set_animals in one_list_animals:
    dictionary_unit.update(one_set_animals)
dict_mix = dict(set(dictionary_unit.items()))
print(dict(sorted(dict_mix.items())))

"""
Task 4. 15
Удалить дубликаты из dictionary
"""
before_dict = {
    'id1':
    {
        'name': 'Ruslan',
        'class': 1,
        'subjects': {'Math', 'Algorithms', 'English'}
    },
    'id2':
        {
            'name': 'Mark',
            'class': 2,
            'subjects': {'Geometry', 'Java', 'Cooking'}
        },
    'id3':
        {
            'name': 'Ruslan',
            'class': 1,
            'subjects': {'Math', 'Algorithms', 'English'}
        }
}
names = []
after_dict = before_dict.copy()
for key, value in before_dict.items():
    if after_dict[key]['name'] not in names:
        names.append(after_dict[key]['name'])
    else:
        after_dict.pop(key)
print(after_dict)

"""
Task 5. 10
Вернуть из dictionary все уникальные values.
Пример
Входные данные = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
Результат = {'S001', 'S005', 'S007', 'S002', 'S009'}
Усложнение! +5 points
Вернуть ту же структуру.
После dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]
"""

list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S002"}, {"VII": "S005"}, {"V": "S009"},
              {"VIII": "S007"}]
uniq = []
L = list_dicts.copy()
for i in list_dicts:
    for key, value in i.items():
        if value not in uniq:
            uniq.append(value)
        else:
            L.remove(i)
print(L)

"""
Task 6. 15 Посчитать общее количество наименований в списке. И только в списках.
Example:
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 
'wednesday': ['manicure', 'hammam', 'beer']}
Результат: 6
"""
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None,
           'wednesday': ['manicure', 'hammam', 'beer']}
count = 0
for i, j in shedule.items():
    if isinstance(j, list):
        count += len(j)
print(count)

"""
Найти официальную документацию по Словарям и прикрепить ссылку к домашней работе +5 points
И попробовать прочитать ).
"""
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

"""
Task 8 . 25 Points
Познакомиться самостоятельно с термином Хеширование.

Ознакомилась на этих ресурсах
https://pythobyte.com/python-hash-function-09311/
https://python-scripts.com/md5-sha1
"""
