from tkinter import *


def click_but(arg):
    value = window.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    window.delete(0, END)
    window.insert(0, value + str(arg))

def operation(arg2):
    value = window.get()
    if value[-1] in "+-/*":
        value = value[:-1]
    elif '+' in value or "-" in value or '*' in value or "/" in value:
        equal()
        value = window.get()
    window.delete(0,END)
    window.insert(0, value + arg2)


def equal():
    value = window.get()
    if value[-1] in "-+*/":
        value = value + value[:-1]
    window.delete(0, END)
    window.insert(0, eval(value))

def clear():
    window.delete(0, END)
    window.insert(0, 0)

tk = Tk()
tk.title("Calculyator 2.0")
tk.geometry("367x400")
tk.resizable(0, 0)
tk.configure(bg="black")

window = Entry(tk, justify=RIGHT, bg="black", fg="white",width=11, font=("Robot", 48))
window.insert(0, "0")
window.place(x=10, y=30)


bt1 = Button(tk, text="1",command=lambda: click_but(1), fg="black",font=("Robot", 20), width=4, height=2).place(x=10, y=320)
bt2 = Button(tk, text="2",command=lambda: click_but(2), fg="black",font=("Robot", 20), width=4, height=2).place(x=95, y=320)
bt3 = Button(tk, text="3",command=lambda: click_but(3),fg="black",font=("Robot", 20), width=4, height=2).place(x=180, y=320)
bt_equal = Button(tk, text="=",command=equal, fg="black",font=("Robot", 20), width=4, height=2).place(x=265, y=320)

bt_4 = Button(tk, text="4",command=lambda: click_but(4), fg="black",font=("Robot", 20), width=4, height=2).place(x=10, y=260)
bt_5 = Button(tk, text="5",command=lambda: click_but(5), fg="black",font=("Robot", 20), width=4, height=2).place(x=95, y=260)
bt_6 = Button(tk, text="6",command=lambda: click_but(6), fg="black",font=("Robot", 20), width=4, height=2).place(x=180, y=260)
bt_plus = Button(tk, text="+",command=lambda :operation("+"), fg="black",font=("Robot", 20), width=4, height=2).place(x=265, y=260)

bt_7 = Button(tk, text="7",command=lambda: click_but(7), fg="black",font=("Robot", 20), width=4, height=2).place(x=10, y=200)
bt_8 = Button(tk, text="8",command=lambda: click_but(8), fg="black",font=("Robot", 20), width=4, height=2).place(x=95, y=200)
bt_9 = Button(tk, text="9",command=lambda: click_but(9), fg="black",font=("Robot", 20), width=4, height=2).place(x=180, y=200)
bt_minus = Button(tk, text="-",command=lambda: operation("-"), fg="black",font=("Robot", 20), width=4, height=2).place(x=265, y=200)

bt_C = Button(tk, text="C",command=clear, fg="black",font=("Robot", 20), width=4, height=2).place(x=10, y=140)
bt_0 = Button(tk, text="0",command=lambda: click_but(0), fg="black",font=("Robot", 20), width=4, height=2).place(x=95, y=140)
bt_multiply = Button(tk, text="*", command=lambda: operation("*"), fg="black",font=("Robot", 20), width=4, height=2).place(x=180, y=140)
bt_divide = Button(tk, text="/", command=lambda: operation("/"), fg="black",font=("Robot", 20), width=4, height=2).place(x=265, y=140)

tk.mainloop()

