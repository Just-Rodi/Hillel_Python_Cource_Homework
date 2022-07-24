# step 1 Создать файл (модуль) с примерами всех методов строк.

example_text = str('My name is Rodi')
example_text_format_map_1 = str('My {name} is {Rodi}')
example_for_format_map_2 = {'name': 'favorite', 'Rodi': 'Python'}
example_for_translation = example_text.maketrans('R', 'r')

print(example_text.capitalize())
print('groß'.casefold() == 'gross')
print(example_text.center(30, '*'))
print(example_text.count('a'))
print(example_text.encode(encoding='utf-8'))
print(example_text.endswith('rodi'))
print('ex\tample\ttext'.expandtabs(tabsize=8))
print(example_text.find('n'))
print(format(10, '+'))
print(example_text_format_map_1.format_map(example_for_format_map_2))
print(example_text.index('a'))
print('HelloWorld2022'.isalnum())
print('hello'.isalpha())
print(example_text.isascii())
print('1000'.isdecimal())
print('10edc00'.isdigit())
print('example_text'.isidentifier())
print('example_text'.islower())
print('2022'.isnumeric())
print(example_text.isprintable())
print('   \t\n\r\t'.isspace())
print('My Name Is Rodi'.istitle())
print('My Name Is Rodi'.istitle())
print('MY NAME IS RODI'.isupper())
print('+'.join(example_text))
print(example_text.ljust(20, '*'))
print(example_text.lower())
print('***example_text'.lstrip('*'))
print(example_text.partition('name'))
print('example text'.removeprefix('ex'))
print('example text'.removesuffix('xt'))
print(example_text.replace('name', 'favorite'))
print(example_text.rfind('m'))
print(example_text.rindex('R'))
print(example_text.rjust(20, '*'))
print(example_text.rpartition('is'))
print(example_text.rsplit(sep=' '))
print(example_text.split(sep=' '))
print('example_text***'.rstrip('*'))
print('example\ntext'.splitlines())
print(example_text.startswith('My'))
print('***example_text***'.strip('*'))
print(example_text.swapcase())
print(example_text.title())
print(example_text.translate(example_for_translation))
print(example_text.upper())
print(example_text.zfill(20))

# step 2 Создать по 3 варинта всех уже изученных объектов в Пайтоне
# строки
name = str('Vladislava')
print('name', name)
surname = str("Rodionova")
print('surname', surname)
profession = str("QA")
print('profession', profession)

# числа(с плавающей точкой, целочисленные)
age = int(23)
print('age', age + 1)
year_of_birth = int(1999)
print('year of birth', year_of_birth - 2)
favorite_number = int(13)
print('favorite number', favorite_number)

example_float_1 = float(5.5)
print(example_float_1)
example_float_2 = float(round(4.76))
print(example_float_2)
example_float_3 = float(9)
print(example_float_3)

# Списки
shop_list_1: list = ['Eggs', 'Apples', 'Tea']
print('You need to buy:', shop_list_1)
years_of_births: list = [1997, 1995, 1992]
print('years of births:', years_of_births)
ex_float_list: list = [4.5, 12.3, 100.6]
print('example float list:', ex_float_list)

# Словари
vocabulary_1: dict = {'apple': 'Яблоко', 'green': 'зелёное'}
print(vocabulary_1['apple'], vocabulary_1['green'])
vocabulary_2: dict = {'sky': 'Небо', 'blue': 'голубое'}
print(vocabulary_2['sky'], vocabulary_2['blue'])
vocabulary_3: dict = {'bird': 'Птица', 'flying': 'Летит'}
print(vocabulary_3['bird'], vocabulary_3['flying'])

# Кортежи
states: tuple = ('England', 'Germany', 'USA')
print(states)
colors: tuple = ('turquoise', 'emerald', 'scarlet')
print(colors)
animals: tuple = ('camel', 'elephant', 'lion')
print(animals)

# step 3 Написать 3 примера использования max(), min()
some_text = 'I will be python developer'
print(ord(max(some_text)), '=', max(some_text))
print(ord(min(some_text)), '=', min(some_text))
some_numbers = '1', '2', '4'
print(ord(max(some_numbers)), '=', max(some_numbers))
print(ord(min(some_numbers)), '=', min(some_numbers))
some_symbols = '!', '$', '@'
print(ord(max(some_symbols)), '=', max(some_symbols))
print(ord(min(some_symbols)), '=', min(some_symbols))

# step 4 выучить какие не изменяемые объекты, а какие изменяемые
""" Изменяемые типы данных: list,dict,set
Неизменяемые типы данных: int, float, complex, str, tuple, bool, none"""

# step 5/6 Написать 3 примера различных с оператором in / написать 3 примера условия if elif else.
user_email = input('Write your email\t')
if '@gmail' in user_email:
    print('I know that your email is registered with Google')
elif '@yahoo' in user_email:
    print('I know that your email is registered with Yahoo')
else:
    print('I don\'t know where you registered email')

user_answer = input('Write the biggest animal\t')
if 'whale' in user_answer:
    print('This is the largest sea animal')
elif 'elephant' in user_answer:
    print('It is the largest land animal')
else:
    print('I don\'t know such an animal')

user_choice = input('What do you prefer, tea or coffee?\t')
if 'coffee' in user_choice:
    print('Congrats you have great taste')
elif 'tea' in user_choice:
    print('Congrats you have not bad taste')
else:
    print('Perhaps you prefer a different drink')
