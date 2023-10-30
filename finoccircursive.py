def fibo(a):
    if a<=0:
        return 0
    elif a==1:
        return 0
    elif a==2:
        return 1
    elif a==3:
        return 2
    else:
        return fibo(a-2)+fibo(a-1)
print(fibo(10))
