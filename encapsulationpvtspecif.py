class parent:
    __a=None
    __b=None
    __c=None
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def swim(self):
        print(self.__a)
        print(self.__b)
        print(self.__c)
    def get(self):
        self.swim()
obj=parent("this is","pyt",66)
obj.get()