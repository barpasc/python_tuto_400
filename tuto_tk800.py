#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import * #GUI package
from tkinter import messagebox
import sqlite3 as sq #For tables and database

con = sq.connect('Courses.db') #dB browser for sqlite needed
c = con.cursor() #SQLite command, to connect to db so 'execute' method can be called

w = Tk() # // main window
# Gets the requested values of the height and widht.
windowWidth = w.winfo_reqwidth()
windowHeight = w.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(w.winfo_screenwidth()/2 - windowWidth/2-180)
positionDown = int(w.winfo_screenheight()/3 - windowHeight/3)

print("Width",windowWidth,"Height",windowHeight)
print("Width",positionRight,"Height",positionDown)

w.title("Course selection")
w.geometry('500x320+0+0') #Width x Height
w.geometry("+{}+{}".format(positionRight, positionDown))

fname = StringVar(w)
lname = StringVar(w)
age = StringVar(w)

#w.L1 = Label(w, text="First Name").grid(row=0,column=0, padx = 5, pady = 10)
w.L1 = Label(w, text="First Name")
w.L1.place(x=20,y=10)

w.e1 = Entry(w, textvariable=fname)
w.e1.place(x=120,y=10)
#w.e1.grid(row=0, column=1)

#w.L2 = Label(w, text="Last Name").grid(row=1,column=0, padx = 0, pady = 3)
w.L2 = Label(w, text="Last Name").place(x=20,y=40)
w.e2 = Entry(w, textvariable=lname)
#w.e2.grid(row=1, column=1)
w.e2.place(x=120,y=40)

#w.L3 = Label(w, text="Age").grid(row=2,column=0, padx = 0, pady = 0)
w.L3 = Label(w, text="Age").place(x=20,y=70)
w.e3 = Entry(w, textvariable=age)
#w.e3.grid(row=2, column=1)
w.e3.place(x=120,y=70, width=50)

#w.L5 = Label(w, text="Gender").grid(row=0, column=4)
w.L5 = Label(w, text="Gender").place(x=350, y=10)
w.f1=Frame(w, relief="sunken", borderwidth = 1)
w.v=IntVar()
w.r1=Radiobutton(w.f1, text="Male", variable=w.v, value=1).pack(anchor=W)
w.r2=Radiobutton(w.f1, text="Female", variable=w.v, value=2).pack(anchor=W)
#w.f1.grid(row=1, column=4)
w.f1.place(x=350, y=35)

#w.L6 = Label(w, text="Course Applied for:", wraplength=90).grid(row=4)
w.L6 = Label(w, text="Course Applied for:", wraplength=90).place(x=20,y=150)

# Listbox ...........

w.LB1 = Listbox(w, width = 27, height = 7)
#w.LB1.grid(row=4, column=1)
w.LB1.place(x=120, y=120)

Courses = [
"Quality Management (Adv.)",
"Financial Management (Adv.)",
"Project Management (Adv.)",
"Project Management (Int.)"
]

for idx, item in enumerate(Courses):
    w.LB1.insert(END, item)

# Listbox ...........

#.....................................................................#

def Chk_Prereq():
    EvalInput()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def EvalInput():
    w.fname = w.e1.get()
    w.lname = w.e2.get()
    try:
        w.age = int(w.e3.get())
        #Check for Age
        if w.age < 21:
            messagebox.showwarning("Invalid Age,you are not eligible")
            return
    except:
        #messagebox.showwarning("Invalid Age")
        messagebox.showinfo("Invalid Age", "Invalid AgeB")
    #Check for Gender
    if w.v.get()==1:
        w.str1 = "Dear Mr."
    elif w.v.get()==2:
        w.str1 = "Dear Ms."
    else:
        messagebox.showwarning("Missing Info, Please select the appropriate gender")
        return
    #Check for Prereq Course
    w.name = w.str1 + " " + w.fname + " " + w.lname

    try:
        w.varl1 = w.LB1.get(w.LB1.curselection())

        if w.varl1 == "Quality Management (Adv.)":
            w.prereq = "The prereq for this course is Quality Management (Int)."
            w.flag = 1
        elif w.varl1 == "Financial Management (Adv.)":
            w.prereq = "The prereq for this course is Financial Management (Bas)."
            w.flag = 1
        elif w.varl1 == "Project Management (Adv.)":
            w.prereq = "The prereq for this course is Project Management (Int)."
            w.flag = 0
        else:
            w.prereq = "The prereq for this course is Project Management (Bas)."
            w.flag = 0
        #Check whether Part Time
        if w.var.get() == 1 and w.flag == 0:
            w.str2 = "\nThis course is not available part time."
        elif w.var.get() == 1 and w.flag == 1:
            w.str2 = "\nThis course is available part time."
        else:
            w.str2 = ""
            w.result = w.prereq + w.str2
            messagebox.showinfo(w.name, w.result)

    except:
        w.prereq = "No course selection made"
        w.result = w.prereq
        messagebox.showinfo(w.name, w.result)


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#get func to isolate the text entered in the entry boxes and submit to database
def get():
        print("You have submitted a record")

        c.execute('''CREATE TABLE IF NOT EXISTS coursesdb3(
            FirstName TEXT, LastName TEXT, age INTEGER);''')

        c.execute("INSERT INTO coursesdb3 (FirstName, LastName, age) VALUES (?,?,?)", (fname.get(), lname.get(), age.get()))

        con.commit()
        c.close()
        conn.close()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def Clear():
    w.e1.delete(0,END)
    w.e2.delete(0,END)
    w.e3.delete(0,END)
    w.c.deselect()
    w.L1.select_clear(w.L1.curselection())

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#


def record():
    c.execute('SELECT * FROM coursesdb3') #Select from which ever compound lift is   selected

    w.geometry('780x320+290+200')
    Label(w, text="current records").place(x=500, y=10)
    w.f2 = Frame(w, borderwidth = 1)
    #w.f2.grid(row=1, column=5)
    w.f2.place(x=500,y=35)

    #w.LB2 = Listbox(w.f2,  width = 25, height = 20,font=("arial", 12))
    w.LB2 = Listbox(w.f2, height = 10,  width = 25,font=("arial", 12))
    w.LB2.pack(side = LEFT, fill = X)
    #w.LB2.grid(row=2, column=5)


    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set)


    Lb.insert(0, 'Date, Max Weight, Reps') #first row in listbox

    data = c.fetchall() # Gets the data from the table

    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box

    L7 = Label(window, text = compdb.get()+ '      ',
               font=("arial", 16)).place(x=400,y=100) # Title of list box, given which compound lift is chosen

    L8 = Label(window, text = "They are ordered from most recent",
               font=("arial", 16)).place(x=400,y=350)
    con.commit()


#.....................................................................#

w.f2=Frame(w)
w.btn1=Button(w.f2, text ="Prerequisites", width=10, command=Chk_Prereq).pack()
# w.btn1=Button(w.f2, text ="Prerequisites", width=10, command=Chk_Prereq)
# w.btn1.place()

w.btn2=Button(w.f2, text ="Save2db",  width=10, command=get).pack()
# w.btn2=Button(w.f2, text ="Validate2Db",  width=10, command=get)
# w.btn2.place()

w.btn3=Button(w.f2, text ="Clear",  width=10, command=Clear).pack()
# w.btn3=Button(w.f2, text ="Clear",  width=10, command=Clear)
# w.btn3.place()

w.btn4=Button(w.f2, text ="Open db",  width=10, command=record).pack()
# w.btn4=Button(w.f2, text ="Open db",  width=10, command=record)
# w.btn4.place()

#w.f2.grid(row=4, column=4)
#w.f2.grid(row=4, column=4, padx = 5, pady = 20)
w.f2.place(x=350,y=120)

#Label(w, text="aaa").grid(row=5)
Label(w, text="").place(x=10,y=280)
w.var=IntVar()
w.c=Checkbutton(w, text="Part-Time Course", variable=w.var, offvalue=0, onvalue=1)
#w.c.grid(row=7, column=0)
w.c.place(x=20, y=300)

w.mainloop() #mainloop() -> make sure that w stays open
