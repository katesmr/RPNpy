#!/usr/bin/python
import os
import sys
import validator
import RPN
from tkinter import Tk, Frame, Entry, Button, END, messagebox, Checkbutton, IntVar

BACK_UP_NAME = ".lres_backup"


def on_exit(entry):
    try:
        with open(BACK_UP_NAME, 'w') as backup:
            backup.write(entry.get())
    except (OSError, IOError):
        pass
    root.destroy()


def solve(_):
    try:
        res = RPN.run(validator.split_expression(expression_input.get()))
        expression_input.delete(0, END)
        expression_input.insert(0, res)
    except Exception as err:
        messagebox.showerror("There was an error:", err)


def add():
    try:
        with open(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\autorunRPN.bat", "w") as autorun:
            autorun.write("python D:\PyProjects\SAPKIS\RPNcalculator\main.py %*")
    except (OSError, IOError) as err:
        messagebox.showerror("There was an error:", err)


if '__main__' == __name__:
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(200, 70))

    input_field_frame = Frame(root)
    input_field_frame.pack()
    button_frame = Frame(root)
    button_frame.pack()

    expression_input = Entry(input_field_frame, width=20)
    expression_input.pack()

    if os.path.isfile(BACK_UP_NAME):
        try:
            with open(BACK_UP_NAME, 'r') as backup:
                expression_input.insert(0, backup.read())
        except (OSError, IOError):
            pass

    run_button = Button(button_frame, text="SOLVE")
    run_button.bind("<Button-1>", solve)

    CheckVar1 = IntVar()
    adding_button = Checkbutton(button_frame, text="Add to autoloading", variable=CheckVar1, onvalue=1, offvalue=0, command=add)

    run_button.pack()
    adding_button.pack()

    root.protocol('WM_DELETE_WINDOW', lambda: on_exit(expression_input))

    root.mainloop()
