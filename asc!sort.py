L=[]
N1=int(input("enter the number"))
for i in range(1,N1+1):
    value=int(input("enter the number"))
    L.append(value)
for i in range (N1):
    for j in range(i+1,N1):
        if(L[i]>L[j]):
            temp=L[i]
            L[i]=L[j]
            L[j]=temp
print(L)