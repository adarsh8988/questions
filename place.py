# import tkinter as tk
# obj=tk.Tk()
# obj.geometry("500x300")
# obj.title("Place")
# lbl=tk.Label(obj,text="this is a car",font=("robort",20,"bold"))
# lbl.place(x=50,y=100)
# lbl=tk.Checkbutton(obj,text="this is a car",font=("robort",20,"bold"),bg="red")
# lbl.place(x=300,y=60)
# obj.mainloop()

import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess

con=mysql.connector.connect(host="localhost",username="root",password='Akarsh!@2001')
curser=con.cursor()

db_name="form"
curser.execute(f"create database if not exists {db_name}")
zx=curser.fetchone()
con.database=db_name



if not list:
    # curser.execute(f"use {db_name}")
    table_name="todo(Title varchar(50),description varchar(100))"
    curser.execute(f"create table {table_name}")
    con.commit()
    
curser.execute("select * from todo")
zx=curser.fetchall()
# print(zx)

def myfun():
    db_title=en1.get()
    db_description=en2.get()
    curser.execute(f"insert into todo values('{db_title}','{db_description}')")
    # print(f"{db_title} {db_description}")
    con.commit()
    
fil=tk.Tk()
fil.geometry("600x500")
fil.config(bg="blue")

frame=tk.Frame(fil,relief="ridge",borderwidth=10)
frame.pack(pady=10)

lbl=tk.Label(frame,text="My To do",font=("robort",10,"bold"))
lbl.pack()


frame1=tk.Frame(fil,relief="ridge",borderwidth=10)
frame1.pack(pady=10)

lbl1=tk.Label(frame1,text="Title",font=("robort,10,bold"))
lbl1.grid(row=1,column=1)

lbl2=tk.Label(frame1,text="Description",font=("robort,10,bold"))
lbl2.grid(row=2,column=1)

lbl1=tk.Label(frame1,text=":",font=("robort,10,bold"))
lbl1.grid(row=1,column=2)

lbl2=tk.Label(frame1,text=":",font=("robort,10,bold"))
lbl2.grid(row=2,column=2)

en1=tk.Entry(frame1)
en1.grid(row=1,column=3)
en2=tk.Entry(frame1)
en2.grid(row=2,column=3)

btn=tk.Button(frame1,text="Submit",font=("robort",10,"bold"),bg="red",command=myfun)
btn.grid(row=3,column=3,pady=5)


frame2=tk.Frame(fil,relief="ridge",borderwidth=10)
frame2.pack(pady=10)

lbl=tk.Label(frame2,text="All To do",font=("robort",10,"bold"))
lbl.pack()


tree=ttk.Treeview(frame2,columns=("sr.no","Title","Description"))
tree.pack()
tree.heading("#0",text="sr.no")
tree.heading("#1",text="Title")
tree.heading("#2",text="Description")


x=0
for i in zx:
    x=x+1   
    tree.insert("","end",text=(x),values=(i))



# l1=tk.Label(frame2,text=1,font=("robort",5,"bold"))
# l1.grid(row=1,column=1)


fil.mainloop()