a=5
for i in range(a):
    for j in range(0,a-i):
        print(" ",end="")
        for k in range(0,j+1):
            print("*",end="")
    print()