class grandparent():
    def __init__(self):
        print("this refers to grandparent")
    def get(self):
        print("this is grandparents getfuc")
class parent(grandparent):
    def __init__(self):
        print("this refers to parent")
        super().__init__()
    def get(self):
        print("this is parents getfunc")
        super().get()
class child(parent):
    def __init__(self):
        print("this refers to child")
        super().__init__()
    def get(self):
        print("this is childs getfunc")
        super().get()
a1=child()
a1.get()