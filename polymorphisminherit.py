class grandparent():
    def set(self):
        print("this is grand parent class")
class parent(grandparent):
    def set(self):
        print("this is parent class")
class child(parent):
    def set(self):
        print("this is child class")
class grandchild(child):
    def set(self):
        print("this is grandchild class")
a1=grandparent()
a1.set()

a2=parent()
a2.set()

a3=child()
a3.set()

a4=grandchild()
a4.set()