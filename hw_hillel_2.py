user_name = input('Fill up your username \t')
age = int(input('Fill up your age \t'))
if age == 16:
    print('Dear', user_name, 'need to wait one year')

elif age > 121:
   print('You are not real', user_name,)

elif 70 <= age <= 90:
    print('You are lucky', user_name, 'and welcome')

elif age > 16:
    print('Welcome', user_name,'on our website')

else:
    print("I'm sorry", user_name, "you are too young")
