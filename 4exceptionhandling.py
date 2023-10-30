def exception(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError as e:
        print(e)
    else:
        print(c)
try:
    exceptio(23,34)
except NameError as e:
    print(e)
exception(10,10)
exception(22,12)