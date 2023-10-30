class arithmatic():
    var1=int(input("enter the 1st var"))
    var2=int(input("enter the 2nd var"))
    def add(self):
        c=self.var1+self.var2
        print(c)
    def condition(self):
        if (self.var1>self.var2):
            print("var1 is greater thane var2")
        else:
            print("var2 is greater")
    def amstrong(self):
        sum1=0
        temp=0
        rem=0
        temp=self.var1
        while(self.var1!=0):
            rem=self.var1%10
            sum1+=rem**3
            self.var1=self.var1//10
        if(temp==sum1):
            print("this is amstrong")
        else:
            print("this is not an amstrong")
art=arithmatic()
art.amstrong()
art.add()
art.condition()
