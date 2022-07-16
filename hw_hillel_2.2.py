user_name = input('Enter your name \t')
print('Hello,', user_name, ', perform one mathematical operation and one comparison operation')
print('First you do the mathematical operation')
number_1 = int(input('Please enter the first number \t'))
action_m = (input('Please enter a mathematical action \t'))
number_2 = int(input('Please enter the second number \t'))

if action_m == '+':
    print('Answer', number_1 + number_2)

elif action_m == '-':
    print('Answer', number_1 - number_2)

elif action_m == '*':
    print('Answer', number_1 * number_2)

elif action_m == '/':
    print('Answer', number_1 / number_2)

elif action_m == '%':
    print('Answer', number_1 % number_2)

elif action_m == '**':
    print('Answer', number_1 ** number_2)

elif action_m == '//':
    print('Answer', number_1 // number_2)

else:
    print('Sorry, you entered a non-math option')

print('Great,', user_name, ', passed the first test')
print('Now enter data for comparison')

number_1_1 = int(input('Please enter the first number \t'))
number_2_2 = int(input('Please enter the second number \t'))
if number_1_1 > number_2_2:
    print(number_1_1, '>', number_2_2)

elif number_1_1 < number_2_2:
    print(number_1_1, '<', number_2_2)

elif number_1_1 == number_2_2:
    print(number_1_1, '=', number_2_2)

print('Thank you,', user_name, ',for taking the time for me. Have a good day :)')
