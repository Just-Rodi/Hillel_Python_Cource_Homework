""" Спросить у пользователя год рождения.
Спомощью if -elif-else
Проверить встроенным строковым методом, состоит ли возраст из числа или текста.
если текст то по попросить ввести число.
Если 21 год вывести “You should visit Holland.”
Если больше 21 вывести “You should visit Vietnam.”
Все остальные варианты. Вывести “Travell everywhere”
"""

user_birth_year = input('Please, write you year of birth\t')
actual_year = 2022
if user_birth_year.isdigit() is True:
    user_age = actual_year - int(user_birth_year)
    if user_age == 21:
        print('You should visit Holland.')
    elif user_age > 21:
        print('You should visit Vietnam.')
    else:
        print('Travel everywhere')
else:
    print('Please enter age as a number')
