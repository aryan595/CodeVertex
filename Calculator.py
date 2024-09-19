def Addition(x,y):
    return x+y
def Multiplication(x,y):
    return x*y
def Division(x,y):
    if y!=0:
        return round(x/y,4)
    else:
        return "Undefined"
def Subtraction(x,y):
    return x-y

def Validation(a):
    try:
         float(a)
         return True
    except ValueError:
        return False        
   
print("Basic Arithmetic Calculator")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Subtraction")

while True:
    a=input("Enter 1st number:")
    if Validation(a):      
        b=input("Enter 2nd number:")
        if Validation(b):
            operation=(input("Enter Operation (1/2/3/4):"))
            if operation.isdigit() and 1<=int(operation)<=4:
                a=float(a)
                b=float(b)
                operation=int(operation)
                if operation==1:
                        result=Addition(a,b)
                elif operation==2:
                        result=Multiplication(a,b)
                elif operation==3:
                        result=Division(a,b)
                elif operation==4:
                        result=Subtraction(a,b)
                else:
                        result="Invalid Operation"

                print("Ans:",result)
                break
            else:
                print("Please enter any above mentioned number:")
        else:
            print("Please enter a number")
    else:
        print("Please enter a number")