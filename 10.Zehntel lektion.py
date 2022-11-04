#1
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.capitalize())
        
#2
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car)
#        print(car.capitalize())
    else:
        print(car.upper())

#3
user=input("Please type your login in this gap\n>>>")
if user=='admin':
    print('Welcome administrator, do you wanna see our users?')
else:
    print(f'Hi {user} welcome to our vlog')
   
number1=input("Please write two numbers.\n>>>1st number-")
number2=input("\n>>>2nd number-")
number1=float(number1)
number2=float(number2)
if type(number1) and type(number1)  is float:
    if number1==number2:
        print("They are equal")
    else:
        print('They are different')
else:
    print('You should give only numbers')