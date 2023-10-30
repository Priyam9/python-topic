class parent():
    def show(self):
        print("this is parent class")
class child(parent):
    def print(self):
        print("this is  child class")
a=child()
a.show()
a.print()