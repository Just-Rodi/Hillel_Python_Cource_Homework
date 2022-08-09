"""
В другом файлике
сделать пример функции
без return c pass or ...
сделать 5 различных функций на свое усмотрение.
"""

# 1)без return c pass or ...

from random import randint


def fun_ex1():
    pass


def fun_ex2(text: str = "Hello World"):
    print(text)


# 2) сделать 5 различных функций на свое усмотрение.

def fun1(username: str):
    pred_int: int = randint(1, 200)
    if pred_int % 2 == 0:
        return print(f'{username}, Luck smiles on you today')
    else:
        return print(f'{username}, Today is not your day, try tomorrow')


def fun2(user_age: int):
    if user_age >= 18:
        return print('Good')


def fun3(pocket_money: int, earned: int, spent: int) -> int:
    return (pocket_money + earned) - spent


def fun4(num: int) -> int:
    if num >= 0:
        return num
    else:
        return -num


def fun5(name: str, age: int):
    if age > 120 or age < 1:
        return print("Invalid age")
    print(f"Name: {name}  Age: {age}")


fun_ex1()
fun_ex2()
fun1('Rodi')
fun2(50)
print(fun3(10, 82, 222))
print(fun4(-1234))
fun5('Rodi', 25)
