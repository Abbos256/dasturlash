#nesting
jobs={'name':'Steve Paul Jobs',
        'job':'Entrepreneur',
        'Education':'Reed college',
        'livedpleaces':' USA,California'
        }
gandhi={'name':'Mohandas Karamchand Gandhi',
          'job':'Lawyer and politician',
          'Education':'Samaldas Arts College',
          'livedpleaces':'India'
          }
einstein={'name':'Albert Einstein',
               'job':'Physicist',
               'Education':'University of Zurich',
               'livedpleaces':'Germany,Swistzerland'}
personalities=[jobs,gandhi,einstein]
per1=jobs
per2=gandhi
per3=einstein
pers=personalities
#print(per1)
#2 Pard of code
for per in pers:
    print(f"name- {per['name']} " 
          f"job- {per['job']} "
          f"Education - {per['Education']}{per['livedpleaces']} " )

#second task
books={'Richard':['The Godfather','Atomic habits'],
       'Adam':['You are unique','Our Memories'],
       'Thatme':['Ghosts walk at night','Devils place']
       }

  

for bookreader,booklist in books.items():
    print(f"\n{bookreader},'loves reading:")
    for books in booklist:
        print(books)
        
#3rd task
countries={
    'germany':
    {'cap':'Berlin',#cap=capital
    'lang':'German',#lang=lnguage
    'wcw':'4 times'#world cup winner
    },
    'usa':{
     'cap':'Washington',
     'lang':'English',
     "wcw":"zero"
     },
    'brasil':
        {
        'cap':'brasil',
        'lang':'Portugal',
        'wcw':'zero'},
        }
for coun,info in countries.items():
    if coun=='usa':
        coun=coun.upper()
    else:
        coun=coun.title()
    print(f"Country name:  {coun}\nIts capital is {info['cap']}\nAnd they speak {info['lang']}\n{coun} won WorldCup {info['wcw']}\n")
    


#4 task
countries={
    'germany':
    {'cap':'Berlin',#cap=capital
    'lang':'German',#lang=lnguage
    'wcw':'4 times'#world cup winner
    },
    'usa':{
     'cap':'Washington',
     'lang':'English',
     "wcw":"0"
     },
    'brasil':
        {
        'cap':'brasil',
        'lang':'Portugal',
        'wcw':'0'},
        }

selc=input("Which country do you want to know about? :") 
if selc in countries:
    info=countries[selc]
    print(f"Country: {selc.title()}\n"
          f"Capital: {info['cap']}\n"
          f"Language:{info['lang']}\n"
          f"Winning World cup titles {info['wcw']} \n")
