import random
import string

def password(length,random_char):
    return ''.join(random.choice(random_char) for _ in range(int(length)))

def complexity(str):
    if str=='low':
        random_char=string.ascii_lowercase+string.digits
    elif str=='moderate':
        random_char=string.ascii_lowercase+string.ascii_uppercase+string.digits
    elif str=='high':
        random_char=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    else:
        print("Error! Enter appropriate option")
    return random_char

while True:
    codelength =(input("Enter length: "))
    if codelength.isnumeric():
        print("Complexity:")
        print("1.low")
        print("2.moderate")
        print("3.high")
        a=input("Enter Password Complexity:")
        if a=='low' or a=='moderate' or a=='high':
            random_char=complexity(a)
            code=password(codelength,random_char)
            print(code)
            break
        else:
            print("Enter correct option")
    else:
        print("Please enter a positive number")
