def createlist():
    a=input("Enter the data:")
    print("Added succcesfully!")
    return a

def scanlist(str,list1):
    if str in list1:
        return True
    else:
        return False 


def modifylist():
    print("1.Change the entries")
    print("2.Delete the entry")
    b=int(input("Enter your choice(1/2):")) 
    if b==1:
        c=input("Which entry you want to change:")
        if scanlist(c,mylist):
            d=mylist.index(c)
            e=input("Enter the new Entry:")
            mylist[d]=e
            print("Modified Successfully!")
        else:
            print("Entry not found")
    elif b==2:
        f=input("Which entry you want to delete:")
        if scanlist(f,mylist):
            mylist.remove(f)
            print("Deleted Successfully!")
        else:
            print("Entry not found")

def showlist(mylist):
    print(mylist)

def savelist(mylist):
    with open('ToDoList.txt','w') as file:
        file.write('\n'.join(mylist))

def loadfile():
    try:
        with open('ToDoList.txt','r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("File not found")
        return []


print("1.Create a list")
print("2.Modify the list")
print("3.Show the list")
print("4.Save and Exit")
mylist=loadfile()

while True:


    option=int(input("Choose the Option:"))

    if option==1:
        a=createlist()
        mylist.append(a)
    elif option==2:
        modifylist()
    elif option==3:
        showlist(mylist)
    else:
        savelist(mylist)
        break