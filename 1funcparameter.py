para=input("enter the operator")
a=float(input("enter the number"))
b=float(input("enter the number"))
def add(a,b):
    print("the addition of numbers is",(a+b))

def sub(a, b):
     print("the subtraction of numbers is", (a-b))

def mul(a, b):
    print("the multiplication of numbers is", (a*b))

def div(a, b):
     print("the division of numbers is", (a/b))

def mod(a,b):
    print("the mod of numbers is",(a%b))

if(para=="add"):
    add(a,b)

if(para=="sub"):
    sub(a,b)

if(para=="mul"):
    mul(a,b)

if (para == "div"):
    div(a,b)

if (para == "mod"):
    mod(a, b)

