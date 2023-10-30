f1=open("/home/student/Desktop/hello.txt","w")
try:
    for i in f1:
        print(i)
except IOError as e:
    print("this is input output error",e)