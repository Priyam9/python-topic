import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='pri7077')
cursor=mydb.cursor()
#cursor.execute("create database pri7077")
#cursor.execute("Show databases")
#for i in cursor:
#    print(i)
#cursor.execute("create table pyt66(id int primary key,name varchar(10),rollno int)")
#cursor.execute("insert into pyt66(id,name,rollno)values(1,'priyam',1),(2,'neeraj',2),(3,'sandesh',3),(4,nitish',4)")
cursor.execute("insert into pyt66(id,name,rollno)values(7,'shubham',7)")

mydb.commit()

