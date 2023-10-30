class grandparent:
    def firstfunc(self,a=10,b=30):
        print(a+b)
class parent1:
    def greet(self,a,b):
        print("this is parent1 and good evening",a+b)
class parent2(grandparent):
    def sayhi(self,a,b):
        print("how are you",a+b)
class grandchild(parent1,parent2):
    def saybye(self):
        print("bye bye")
a=int(input("enter any number"))
b=int(input("enter any number"))
obj=grandchild()
obj.greet(a,b)
obj.sayhi(a,b)
obj.saybye()
obj.firstfunc()