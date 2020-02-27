import webbrowser
from tkinter import *
from tkinter import messagebox
import mysql.connector as con
import sample

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "MYSQL123",
    db = "login"
)
cur = mydb.cursor()

top = Tk()
top.geometry("400x250")
#text =Label(top,text ="Login").place(x=20,y=120)
name = Label(top,text="Name").place(x=30,y=50)
password = Label(top,text="Password").place(x=30,y=90)
e1_id = StringVar()
e1 = Entry(top,textvariable=e1_id).place(x=120,y=50)
e2_id = StringVar()
e2 = Entry(top,textvariable=e2_id).place(x=120,y=90)
#print(e1_id.get())

def sub():
    cur.execute("select * from log")
    res = cur.fetchall()
    test = 0

    for a,b,c,d in res:
        if a==e1_id.get() and d==str(e2_id.get()):
            test=1
            break
        else:
            test=0

    if test==1:
        messagebox.showinfo("Sucess","Successfully logged in")
    else:
        messagebox.showwarning("Error","wrong name and password")
btn = Button(top,text="Submit",command=sub).place(x=120,y=130)

def register():
    reg1 = sample()
    reg1.register()
    # #messagebox.showerror("not submit")
    # top = Tk()
    # top.geometry("400x250")
    # #text =Label(top,text ="Login").place(x=20,y=120)
    # name = Label(top,text="Name").place(x=30,y=30)
    # email = Label(top,text="E-mail").place(x=30,y=60)
    # phno = Label(top,text="Phno.").place(x=30,y=90)
    # password = Label(top,text="Password").place(x=30,y=120)
    #
    # e3_id = StringVar()
    # e3 = Entry(top,textvariable=e3_id).place(x=120,y=30)
    # e4_id = StringVar()
    # e4 = Entry(top,textvariable=e4_id).place(x=120,y=60)
    # e5_id = IntVar()
    # e5 = Entry(top,textvariable=e5_id).place(x=120,y=90)
    # e6_id = StringVar()
    # e6 = Entry(top,textvariable=e6_id).place(x=120,y=120)
    # print(e3_id.get(),e4_id.get(),e5_id.get(),e6_id.get())
    # def sub1():
    #     sql = "insert into log(name,email,phno,password) values(%s,%s,%s,%s)"
    #     print( e3_id.get(),e4_id.get(),e5_id.get(),e6_id.get())
    #     val = (e3_id.get(),e4_id.get(),e5_id.get(),e6_id.get())
    #     cur.execute(sql,val)
    #     mydb.commit()
    #     messagebox.showinfo("Successfully submited","Successfully submitted")
    # btn = Button(top,text="Submit",command=sub1).place(x=120,y=150)
    # print(e3_id.get(),e6_id.get())
    # top.mainloop()


reg = Button(top,text="Register",command=register).place(x=200,y=130)

top.mainloop()