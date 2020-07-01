from pip._vendor.distlib.compat import raw_input
 
groceryList = []
def showMenu():
    print("1 - Add item to grocery list")
    print("2 - Delete item to grocery list")
    print("3 - Show the grocery list")
    print("4 - Exit")
    action = int(input("Please, enter one of the options: "))
    return action

def addItem():
    newItem = raw_input("Please, enter to name of the  item you want to add: ")
    groceryList.append(newItem)

def deleteItem():
    nameItem = raw_input("Please, enter to name of the  item you want to delete:")
    index = -1
    found = False
    for element in groceryList:
        index += 1
        if element == nameItem:
            found = True
            break
    if (found):
        del groceryList[index]
def listItens():
    for element in groceryList:
        print (element)

while True:
    action = showMenu()
    if action == 4:
        break
    elif action == 3:
        listItens()
    elif action == 1:
        addItem()
    elif action == 2:
        deleteItem()

