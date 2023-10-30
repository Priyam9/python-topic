import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['empname'])
    e3.insert(0,select['mobileno'])
    e4.insert(0,select['salary'])

def Add():
    studid=e1.get()
    studname=e2.get()
    coursename=e3.get()
    feee=e4.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",
                                    database="mypayroll")
    mycursor=mysqldb.cursor()

    try:
        sql="INSERT INTO registration (id,empname,mobileno,salary) VALUES (%s,%s,%s,%s)"
        val=(studid,studname,coursename,feee)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("Information","Employee Insterted Sucessfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def Update():
    studid=e1.get()
    studname=e2.get()
    coursename=e3.get()
    feee=e4.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",
                                    database="mypayroll")
    mycursor=mysqldb.cursor()

    try:
        sql="Update registration set empname = %s,mobileno = %s where id = %s"
        val=(studname,coursename,feee,studid)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("Information","Record Updated Sucessfully")

        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def Delete():
    studid = e1.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root",
                                      database="mypayroll")
    mycursor = mysqldb.cursor()

    try:
        sql = "Delete from registration where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Information", "Record Deleted Sucessfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def Search():
    studid = e1.get()
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="root"
                                      ,database="mypayroll")
    mycursor=mysqldb.cursor()
    lastid=mycursor.lastrowid

    try:
        sql = "Search from registration where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Information", "Search Sucessfull")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def Show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root",
                                      database="mypayroll")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,empname,mobileno,salary from registration")
    records=mycursor.fetchall()
    print(records)
    for i,(id,stname,course,fee) in enumerate(records,start=1):
        listBox.insert("","end",values=(id,stname,course,fee))
        mysqldb.close()

root=Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root,text="EmployeeRegistration",fg="red",font=(None,30)).place(x=300,y=5)
tk.Label(root,text="Employee ID").place(x=10,y=10)
Label(root,text="Employee Name").place(x=10,y=40)
Label(root,text="Mobile").place(x=10,y=70)
Label(root,text="Salary").place(x=10,y=100)

e1=Entry(root)
e1.place(x=140,y=10)

e2=Entry(root)
e2.place(x=140,y=40)

e3=Entry(root)
e3.place(x=140,y=70)

e4=Entry(root)
e4.place(x=140,y=100)

Button(root,text="Add",height=3,width=13,command=Add).place(x=30,y=130)
Button(root,text="Update",height=3,width=13,command=Update).place(x=140,y=130)
Button(root,text="Delete",height=3,width=13,command=Delete).place(x=250,y=130)
Button(root,text="Search",height=3,width=13,command=Search).place(x=360,y=130)


cols=('id','empname','mobileno','salary')
listBox = ttk.Treeview(root,columns=cols,show='headings')#Like columns
for col in cols:
    listBox.heading(col,text=col)
    listBox.grid(row=1,column=0,columnspan=2)
    listBox.place(x=10,y=200)

Show()
listBox.bind('<Double-Button-1>',GetValue)#DOUBLE CLICK ON BLUE LINE HIGLIGHT FOR GETTING VALUE

root.mainloop()


