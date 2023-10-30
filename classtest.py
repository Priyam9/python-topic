def classtest(a):
    d={"UPPERCASE":0,"LOWERCASE":0}
    for i in a:
        if i.isupper():
            d["UPPERCASE"]+=1
        elif i.islower():
            d["LOWERCASE"]+=1
    print("no of uppercase letters in string",d["UPPERCASE"])
    print("no of lowercase letters in string",d["LOWERCASE"])
classtest("The qick Brow Fox")