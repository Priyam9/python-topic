from abc import ABC
class p1(ABC):
    def get(self):
        pass
class child1(p1):
    def get(self):
        print("this is child 1 class")
class child2(p1):
    def get(self):
        print("this is child 2 class")
class child3(p1):
    def get(self):
        print("this is child 3 class")
class child4(p1):
    def get(self):
        print("this is child 4 class")
a1=child1()
a1.get()
a2=child2()
a2.get()
a3=child3()
a3.get()
a4=child4()
a4.get()