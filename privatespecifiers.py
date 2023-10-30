class parent1:
    __a=100
    pass
a1=parent1()
print(a1._parent1__a)

class parent1:
    __a=100
    __b=200
    def swim(self):
        print(self.__b+self.__a)
obj1=parent1()
obj1.swim()