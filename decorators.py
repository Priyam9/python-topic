def decorator(fx):
    def func(*args,**kwargs):
        print("this is function")
        fx(*args,**kwargs)
    return func
def mul(a,b):
    print(a*b)
decorator(mul)(2,3)