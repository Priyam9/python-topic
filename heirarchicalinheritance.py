class p1:
    def get(self):
        print("this is parent 1")
class child1(p1):
    def set(self):
        print("this is child 1")
class child2(p1):
    def get1(self):
        print("this is child 2")
class child3(p1):
    def set1(self):
        print("this is child 3")
class child4(p1):
    def kw(self):
        print("this is child 4")
print("child is printing")
obj=child1()
obj.get()
obj.set()

print("child is printing")
obj1=child2()
obj1.get()
obj1.get1()

print("child is printing")
obj2=child3()
obj2.get()
obj2.set1()

print("child is printing")
obj3=child4()
obj3.get()
obj3.kw()