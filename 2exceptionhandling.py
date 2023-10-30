a=100
try:
    b=a/0
    print(b)
except:
    print("divide by zero")
finally:
    print("this is necessary")