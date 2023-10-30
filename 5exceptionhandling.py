try:
    a=int(input("enter the number"))
    if(a>10):
        print("vote")
    else:
        print("no vote")
except ValueError as e:
    print("please enter the correct values",e)