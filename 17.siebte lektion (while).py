#17
#while
favorite_books=[]
fbooks=favorite_books
stop_words=['STOP','EXIT',' ','  ','',0,1,2,3,4,5,6,7,8,9]
print("Give a name of your favorite books (If you type \"STOP\" or number 0 to 9 or just space the program complete asking)")
while True:
    book=input('Your lovely book: ').upper()
    if book in stop_words:
        break
    else:
        favorite_books.append(book)
print('Thanks for using') 

#Ticked selling
#their prices are several according to age
print('Type your age and know how much are tickets for you (If you write "stop" or "quit") program will stop.')
while True:
    age=input('AGE:')
    if age=='stop':
        break
    elif age=='exit':
        break
    elif int(age)>65:
        print("Ticket is free for you!")
    elif int(age)<7:
        print("Ticket is 2$")
    elif int(age)<18:
        print("5$ sir")
    elif int(age)<65:
        print("You shoul pay 7$")
    else:
        break
print('Thanks for working with us')

