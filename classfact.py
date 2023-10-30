class factorial():
    a=int(input("enter the number"))
    fact1=1
    def fac(self):
        if(self.a==0):
            print("factorial of 0 is 1")
        elif(self.a==1):
            print("factorial of 1 is 1")
        else:
            for i in range(1, self.a + 1):
                self.fact1 = self.fact1 * i
                print(self.fact1)
a=factorial()
a.fac()
