class person(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemployee(self):
        return False
class employee(person):
    def isemployee(self):
        return True
emp=person("ayush")
print(emp.getname(),emp.isemployee())
emp=person("ayush")
print(emp.getname(),emp.isemployee())