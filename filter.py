l1=[53,4,56,7.89,10,78,5,6,34]
def great(n):
    return n>10
l2=filter(great,l1)
print(list(l2))
