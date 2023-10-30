def generator():
    for i in range(0,10):
        yield i
g=generator()
for j in g:
    print(j)
