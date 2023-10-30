class parent1():
    def hi(self,a):
        self.a=a
        print(" ",self.a)
class parent2():
    def hello(self,b):
        self.b=b
        print(" ",self.b)
class child(parent1,parent2):
    def attach(self):
        print(self.a+self.b)
obj=child()
obj.hi("hi")
obj.hello(" how are you")
obj.attach()
