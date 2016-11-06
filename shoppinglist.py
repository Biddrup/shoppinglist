#This wii keep the database
shoppinglist = {}

#This will help you to find out and
#Update the database
while True:
    #This will take input from user
    print('Enter a name: (blank to quit)')
    #keep in mind input is casesensetive
    #so, 'Biddrup' and 'biddrup' is different from each other
    name = input()
    #If input '', then loop will be terminated
    if name == '':
        break
    
    newname = name.upper()
    #This will check the name in databse or not
     
    if newname in shoppinglist:
        #If the input in databse, this will print
        print (shoppinglist[newname] + ' is needed for this picnic.')
    else:
        print('I do not have the information for ' + name)
        #This will take info under that name
        print('What is the amount')
        items = input()
        newitems = items.upper()
        shoppinglist[name] = newitems
        #And, databse is updated now
        print('Bazzaritems database updated')
for i in shoppinglist.items():
    print(i)
