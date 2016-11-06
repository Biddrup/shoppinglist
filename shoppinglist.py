#This is a database for shopping list
def printshoppinglist(shopdic):
    print('Shopping List'.center(35, '='))
    for k, v in shopdic.items():
        print(k.ljust(20, '.') + 'TK. ' + str(v))
        total = 0
        total = total + int(v)
        print('Total cost = ' + str(total))


shoppinglist = {}

#This will help you to find out shopping items and
#Update the database
while True:
    #This will take input from user
    print('Enter an item: (blank to quit)')
    #This is not case sensetive
    name = input()

    #If input '', then loop will be terminated
    if name == '':
        break

    #This will keep the input as uppercase
    newname = name.upper()
    
    #This will check the name in databse or not 
    if newname in shoppinglist:
        #If the input in databse, this will print
        print('Budget for ' + newname + ' is TK. ' + shoppinglist[newname])
    else:
        print('I do not have the information for ' + newname)
        #This will take info under that name
        print('What is the amount')
        items = input()
        shoppinglist[newname] = items
        #And, databse is updated now
        print('Shoppinglist database updated')
printshoppinglist(shoppinglist)
