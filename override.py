class grandparent():
    def set(self,a,b):
        print(a+b)
class parent1():
    def set(self,a,b):
        print(a*b)
class parent2():
    def set(self,a,b):
        print(a-b)
class child(parent1,parent2):
    def set(self,a,b):
        parent1.set(self,a,b)
        parent1.set(self,a,b)
        grandparent.set(self,a,b)

        if(a<b):
            print("b is greater")
        else:
            print("a is greater")
a=int(input("enter the number"))
b=int(input("enter the number"))
a1=child()
a1.set(a,b)