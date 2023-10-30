class p1:
    def courses(self,course):
        print("name of course")
        self.course=course
        return course
class p2:
    def fees(self,fee):
        print("amount of the course")
        self.fee=fee
        return fee
class p3:
    def student(self,id):
        print("student id")
        self.id=id
        return id
class p4:
    def duration(self,month):
        print("course duration")
        self.month=month
        return month
class data(p1,p2,p3,p4):
    def show(self):
        print(self.course)
        print(self.fee)
        print(self.id)
        print(self.month)
course=input("enter the course you would like")
fee=int(input("enter the course amount"))
id=int(input("enter the student id"))
month=int(input("enter the course duration"))
obj=data()
obj.courses(course)
obj.fees(fee)
obj.student(id)
obj.duration(month)
obj.show()