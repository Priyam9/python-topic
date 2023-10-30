a=int(input("enter a number"))
fact1=1
if(a==0):
    print("factorial of 0 is 1")
elif(a==1):
    print("factorial of 1 is 1")
else:
    for i in range(1,a+1):
        fact1=fact1*i
        print(fact1)