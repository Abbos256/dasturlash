#dictionary
father={
        'name':'Akmal',
        'age':'46',
        'address':'Karshi'}
print(f"My fathers name is {father['name']}, he is {father['age']} and he lives {father['address']}")

#Favourite_meals
#john={'fmeal':'fast_food'}
#kahn={'fmeal':'kfc'}
#jony={'fmeal':'pizza'}
#johnson={'fmeal':'laddoo'}
#jerry={'fmeal':'sandwich'}
#print(f"John favorite food is {john['fmeal']}")
#print(f"kahn favorite food is {kahn['fmeal']}")
#print(f"jony favorite food is {jony['fmeal']}")

python_dictionary={'print':'This is a function that shows what do you want on console','if':'if is a function that works like an algorithm that function enter to one road from several','else':'else also works like a if','int':'it is a type of numbers'}
word=input('Please give a word that you wanna know its meaning\n>>>').lower()
if word in python_dictionary:
    print(python_dictionary[word])
else:
    print('Sorry we do not know this word\'s defination')