"""
1)
Задачи на функцию all()
1. Создать пример со значениями True и False.
2. Создать пример со значениями заменяющими True False.
Любой объект в пайтон можно представить как бул объект. Пример bool( [ ] ) -> False
"""
# 1.1 True
example_list: list = [1, 2, 3]
print("all() examples: ", all(example_list))

# bool example
print(all([bool([1, 2, 3]), bool('qwe'), bool(1)]))

# 1.2 False
example_dict: dict = {0: "Cat", 1: "Dog"}
print("all() examples: ", all(example_dict))

# bool example
print(all([bool([]), bool(''), bool(0)]))

"""
2)
Задачи на функцию any()
Повторить примеры как в функции all().
"""
# 1.1 True
example_list: list = [1, 2, 3]
print("any() examples: ", any(example_list))

# bool example
print(any([bool([1, 2, 3]), bool('qwe'), bool(1)]))

# 1.2 False
example_dict: dict = {0: "Cat", False: "Dog"}
print("any() examples: ", any(example_dict))

# bool example
print(any([bool([]), bool(''), bool(0)]))

"""
3)
Задачи на функцию isinstance()
Создать примеры со всеми известными вами объектами в пайтон.
"""
print("Some basic examples: ")
example_var = isinstance(9, int)
print(example_var)
example_var = isinstance(example_dict, str)
print(example_var)
example_var = isinstance(example_list, list)
print(example_var)
example_var = isinstance(example_dict, dict)
print(example_var)
example_var = isinstance(example_list, tuple)
print(example_var)
example_var = isinstance(5.1, float)
print(example_var)

"""
4)
Прочитать главу 3 рекурсия. Книга Грокаем Алгоритмы. Адитья Бхаргава.
"""


# Решила взять от туда себе простой, но интересный пример
def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


"""
Когда пишется рекурсивная функция, в ней необходимо указывать, в какой момент следует прервать рекурсию. 
Каждая рекурсивная функция состоит из двух частей: базового случая и рекурсивного случая.
В рекурсивном случае функция вызывает сама себя. 
В базовом случае функция себя не вызывает чтобы предотвратить зацикливание.
"""

"""
5)
Написать функцию бутерброд внутри себя определяет другую функцию колбаса и возвращает ее объект
(Пожалуйста не результат выполнения функции, а именно объект функции). 
Если не понятно мое задание то выполнять его не требуется, вместо него прочитать пункты из книги 
'Изучаем Пайтон 4-е издание. Лутц.'
  a. Функции – это объекты: атрибуты и аннотации
  b. Косвенный вызов функций 
"""


def sandwich():
    def sausage():
        pass

    return sausage


print(sandwich())
