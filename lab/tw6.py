import tkinter
from tkinter import *

rootwindow = Tk()
num1 = tkinter.StringVar()
num2 = tkinter.StringVar()
num3 = tkinter.StringVar()

rootwindow.geometry("500x500")
rootwindow.title("Calculator")
label4 = Label()


def add():
    c = int(num1.get()) + int(num2.get())
    num3.set(str(c))


def sub():
    c = int(num1.get()) - int(num2.get())
    num3.set(str(c))


def mul():
    c = int(num1.get()) * int(num2.get())
    num3.set(str(c))


def div():
    c = int(num1.get()) / int(num2.get())

    num3.set(str(c))


def reset():
    num1.set("")
    num2.set("")
    num3.set("")


label1 = Label(rootwindow, text="First Number").place(x=20, y=50)
label2 = Label(rootwindow, text="Second Number").place(x=20, y=100)
label3 = Label(rootwindow, text="Total").place(x=20, y=150)
textfield = Entry(rootwindow, textvariable=num1, width=50).place(x=120, y=50)
textfield1 = Entry(rootwindow, textvariable=num2, width=50).place(x=120, y=100)
textfield2 = Entry(rootwindow, textvariable=num3, width=50).place(x=120, y=150)

b1 = Button(rootwindow, text="+", padx=20, pady=20, command=add, borderwidth=5).place(x=50, y=200)
b2 = Button(rootwindow, text="-", padx=20, pady=20, command=sub, borderwidth=5).place(x=250, y=200)
b3 = Button(rootwindow, text="*", padx=20, pady=20, command=mul, borderwidth=5).place(x=50, y=300)
b4 = Button(rootwindow, text="/", padx=20, pady=20, command=div, borderwidth=5).place(x=250, y=300)
b5 = Button(rootwindow, text="reset", padx=20, pady=15, command=reset, borderwidth=5).place(x=150, y=250)
rootwindow.mainloop()
