class greatgrandparent():
    def laugh(self):
        print("this is great grand parent")
class grandparent(greatgrandparent):
    def walk(self):
        print("this is grand parent")
class parent(grandparent):
    def talk(self):
        print("this is parent")
class child(parent):
    def set(self):
        print("this is child")
class grandchild(child):
    def get(self):
        print("this is grand child")
g1=grandchild()
g1.walk()
g1.talk()
g1.set()
g1.get()
g1.laugh()
