#1 Program which can say that there are things you want in shop or not 
shop_products=['milk','egg','braed','water','cola','pepsi','meat','sugar','oil','dry tea']
things_we_want=[]
for things in range(5):
    things=input('What types of things would you like to buy?\n>>>')    
    things_we_want.append(things)

for things in things_we_want:
    if things in shop_products:
        print(f'Yes we have {things}')
    else:
        print(f'Sorry we do not have {things}')
        
#2
shop_products=['milk','egg','braed','water','cola','pepsi','meat','sugar','oil','dry tea']
things_we_want=[]
for things in range(5):
    things=input('What types of things would you like to buy?\n>>>')    
    things_we_want.append(things)
things_we_have_not=[]
things_we_have=[]
for things in things_we_want:
    if things in shop_products:
        things_we_have.append(things)
    else:
        things_we_have_not.append(things)
        
if len(things_we_have_not)==0:
    print('We have all things you want')
else:
    print("Sorry we do not have:")
n=len(things_we_have_not)
for things in range(n):
    print(things)
    
#3 this login is already in use or not
all_logins=['abbos','java','Abu','ilon','bror']
login_1587=input('Please input your login (it should be new and unused by others)\n>>>')
if login_1587.lower() in all_logins:
    print('This login is already used, please write another one')
else:
    print('Welcome to our world, your login is saved in our archive')
    
#4
number=int(input('Write a number>>>'))
for divisor in list(range(2,11)):
    if number%divisor==0:
        print(f'{number} is divisible by {divisor} without remainder')