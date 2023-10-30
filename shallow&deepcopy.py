import copy
li1=[1,2,[8,3],14]
#li2=copy.deepcopy() while using deep copy one cannot edit OG list
li2=copy.copy(li1)
print("the original")
for i in range(0,len(li1)):
    print(li1[i])
li2[2][0]=7
print("new after deepcopy")
for i in range(0,len(li1)):
    print(li1[i])
print("the original elements after deep copying")
for i in range(0,len(li1)):
    print(li1[i])