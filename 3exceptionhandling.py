try:
    a=open("f1.txt","r")
    for i in a:
        print(i)
except FileNotFoundError as e:
    print("file does not exsist",e)