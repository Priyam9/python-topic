from tkinter import *
from tkinter import  messagebox
root=Tk()
root.geometry("500x400")
l1=Label(root,text="Enter The Number").grid(row=0,column=0)
l2=Label(root,text="Enter The Number").grid(row=2,column=0)

num1=IntVar()
num2=IntVar()
e1=Entry(root,justify=CENTER,textvariable=num1).grid(row=0,column=2)
e2=Entry(root,justify=CENTER,textvariable=num2).grid(row=2,column=2)

l3=Label(root)
l3.grid(row=4,column=2)

l4=Label(root)
l4.grid(row=6,column=2)

l5=Label(root)
l5.grid(row=8,column=2)

def add():
    sum1=num1.get()+num2.get()
    l3.config(text="Addition"+str(sum1))
btn=Button(text="Addition",command=add,justify=CENTER,bg="orange",fg="black",).grid(row=5,column=2)

def sub():
    sum1=num1.get()-num2.get()
    l3.config(text="subtraction"+str(sum1))
btn2=Button(text="subtraction",command=sub,justify=CENTER,bg="orange",fg="black",).grid(row=7,column=2)

def mul():
    sum1=num1.get()*num2.get()
    l3.config(text="multiplication"+str(sum1))
btn3=Button(text="multiplication",command=mul,justify=CENTER,bg="orange",fg="black",).grid(row=9,column=2)
root.mainloop()