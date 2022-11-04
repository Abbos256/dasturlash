#1 The program which indicate number is even or odd
number=int(input('Please type a number and I show that it is odd or even\n>>>'))
if number%2 ==0:
    print('It is even number')
else:
    print('It is not even number, It would be odd')
    
#2
age=int(input("Please write user's age\n>>>"))
if age<=4 or age>=60:
    print('Ticked free for you')
elif age<=18:
    print('You should pay 18$ for ticket')
else:
    print('You should pay 25$ for ticket')
