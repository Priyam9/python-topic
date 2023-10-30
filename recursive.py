def fact(n):
    if(n==0):
        return n
    if(n==1):
        return n
    else:
        return n*fact(n-1)
num=int(input("enter a number"))
print ("this factorial is ",fact(num))
        