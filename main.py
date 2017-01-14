#!/usr/bin/python
import os
import sys
import validator
import RPN
from tkinter import Tk, Frame, Entry, Button, END, messagebox, Checkbutton, IntVar


def solve(_):
    try:
        res = RPN.run(validator.split_expression(expression_input.get()))
        expression_input.delete(0, END)
        expression_input.insert(0, res)
    except Exception as err:
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

    run_button = Button(button_frame, text="SOLVE")
    run_button.bind("<Button-1>", solve)

    run_button.pack()

    root.protocol('WM_DELETE_WINDOW', lambda: root.destroy())

    root.mainloop()
