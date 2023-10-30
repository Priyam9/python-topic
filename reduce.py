from functools import *
l1=[3,5,46,787,90,45]
l2=reduce(lambda  a,b:a+b,l1)
print(l2)
