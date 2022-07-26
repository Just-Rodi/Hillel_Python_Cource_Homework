"""Задача 1. 10 баллов
тема Срезы и условие if.
написать программку которая будет состоять из первых двух и последних символов предоставленной строки.
Если длинна строки меньше двух символов напечатать строку типа.
'Ваша строка слишком короткая - СТРОКА ' . Через метод форматирования строк с %.
Входная строка : 'Hillel school'
Результат1 : 'Hiol'
илb
Результат2 : 'Ваша строка слишком короткая - и ваша строка'
"""

some_string: str = input('Enter text:\t')
if len(some_string) < 2:
    print('Ваша строка слишком короткая - %s' % some_string)
else:
    print(f'{some_string[:2]}{some_string[-2:]}')

""" Задача 2. 15 баллов
Тема Dict
Написать программу, которая подсчитывает количество символов в строке
и формирует dict в котором key = буква, value= количество их в слове:
Входная строка : 'Hillel school'
Результат :  {'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}
"""

some_text: str = input('Enter your text, please:\t')
text_list = list(some_text)
dictionary = {}
for i in text_list:
    dictionary[i] = int(text_list.count(i))
print(dictionary)

"""Задача 3. 15 баллов
Тема list и его методы. Строки и срезы.
Программа принимает список продуктов и принтит самое длинное слово и его длину.
Иcпользовать ''.format() для вывода строки и аргументов.
Входные данные: ['bread', 'milk', 'kolbasa']
Результат: 'Самое длинное название продукта kolbasa длинна 7 символов'
"""

user_list: str = input('Please, enter your product list after space:\t')
product_list = user_list.split(' ')
longest_world = ''
for i in product_list:
    if len(i) > len(longest_world):
        longest_world = i
print('Самое длинное название продукта {0} длина {1}'.format(longest_world, len(longest_world)))

"""
Задача 4. 5 баллов
Пользователь водит свое имя.
Возвращается тектс в БОЛЬШОМ и маленьком регистре. Использовать ' '.format().
Для вставки аргументов в текст.
Входные данные: Apollo
Результат: APPOLLO apollo
"""

users_input: str = input('Please enter your name:\t')
print('{0} {1}'.format(users_input.upper(), users_input.lower()))

"""Задача 5. 15 баллов.
Тема приведение типов. Работа со списком. Расчленение строки и ее соединение.
Пользователь вводит через запятую последовательность слов например цвета или продукты.
Программа возвращает уникальные слова отсортированные по алфавиту.
Входные данные: red, white, black, red, green, black
Результат: black, green, red, white
"""
user_list_input: str = input('Please enter color after comma:\t')
users_list = user_list_input.split(', ')
users_list = list(users_list)
users_list = set(users_list)
print(*sorted(users_list), sep=',')

"""
Задача 6. 5 баллов
Тема Кортеж и работа с ним.
Удалить элемент из кортежа.
Входные данные: (1, 2, 3)
Результат: (1, 2)
"""

some_tuple: tuple = (1, 2, 3)
some_tuple: list = list(some_tuple)
some_tuple.remove(some_tuple[-1])
some_tuple: tuple = tuple(some_tuple)
print(some_tuple)

"""
Задача 7. 10 баллов
Написать программу которая данный список кортежей переведет в список списков
Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
"""

test_value: list = list([(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)])
for i in range(len(test_value)):
    test_v = list(test_value.pop())
    test_value.insert(i, test_v)
print(test_value[::-1])

"""
Задача 8. 15 баллов
Тема range
Есть последовательность от -99 до 99. Ее шаг 3. т.е. [-99, -96]
напечатать все элементы последовательности которые делятся на 3 без остатка.
напечатать в формате 'это <<ЧИСЛО>> делится без остатка на 3'
использовать метод редактирования строки f' строки'
"""

some_range = tuple(range(-99, 99, 3))
for i in some_range:
    print(f'Это число {i} делится без остатка на 3')

"""
Задача 9. 10 баллов
Тема Листы
Даны два списка элементов если хоть один Элемент совпадает отпринтить True.
print(Тrue) не слово! а объект подставить.
"""
list1: list = 'apple, orange, bananas'.split(', ')
list2: list = 'dog, cat, orange'.split(', ')
list3 = []
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
print(list3)
