l1=[1,2,3,4,5,6,7,9]
l2=[1,2,3,4,5,8,6,7]

res=list(filter(lambda x:x[0]!=x[1],zip(l1,l2)))
print(str([r[1] for r in res]))