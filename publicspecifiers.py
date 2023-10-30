class specifiers:
    a=10
    pass
a1=specifiers()
print(a1.a)

class parent1:
    a=100
    b=23
    def swim(self):
        print(self.a+self.b)
a1=parent1()
a1.swim()