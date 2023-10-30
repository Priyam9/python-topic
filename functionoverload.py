from functools import singledispatchmethod
from datetime import date, time


class formatter:
    @singledispatchmethod
    def format(self, arg):
        raise NotImplementedError(f"cannot format value")
    @format.register
    def  _(self,arg:date):
        return f"{arg.day}-{arg.month}-{arg.year}"
    @format.register
    def _(self,arg:time):
        return f"{arg.hour}-{arg.minute}-{arg.second}"
f=formatter()
print(f.format(date(2023,5,18)))
print(f.format(time(16,58,00)))