#this is for reading file only
"""f1=open("/home/student/Desktop/hello.txt","r")
for i in f1:
    print(i)"""
#this is for writing file only
"""f1=open("/home/student/Desktop/hello.txt","w")
f1.write("hi")
f1.close()"""
#this is for append(editing exsiting file) file only
f1=open("/home/student/Desktop/hello.txt","a")
f1.write("how are you")
f1.close()