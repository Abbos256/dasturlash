#    else:
#       orders.append(meal)
#while dictionary 
#e-shopping
print("What do you want to sell, type its name here and please give us its price also\nIf you want to stop the process please type 'no' when we ask\n".upper())
item=True
items={}
while True:
    item=input("Name of item for sale \n(if that is all type stop):")
    if item=='stop':
        print('Thanks for working with us')
        break
    else:
        price=input(f"How much is {item}? -")
        items[item]=price



#while
#order smth
question="What would you like to eat and drink?"
question+="( After ordering please type \"stop\")"
que=question
orders=[]
meal=True
while meal:
    meal=input('Please, type your wishes:')
    orders.append(meal)
    final=input("Anything else? yes|no- ")
    if final=='no':
        print("Thank you for your visit")
        break 
    else:
        print("Ordering going on...")

for item in orders:
    if item in items:
        print(f'We have {item}, it is {items[item]}')
    else:
        print(f'Sorry we have not got a {item}')


#
#separate
orders=['car','phone','watch','house','laptop']
shop_menu={'car':'20,000$','phone':'700$','laptop':'5000$','Gold':'750'}
while orders:
   order=orders.pop()
   if order in shop_menu.keys():
       print(f'{order} is {shop_menu[order]}')
   else:
       print(f'We have not {order}')
    
   
    
   
    
   