#!/usr/bin/python
import validator
import RPN
from tkinter import Tk, Frame, Entry, Button, END, messagebox


def solve(event):
    try:
        res = RPN.run(validator.split_expression(expression_input.get()))
        expression_input.delete(0, END)
        expression_input.insert(0, res)
    except Exception as err:
        messagebox.showerror("There was an error:", err)


if '__main__' == __name__:
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(200, 50))

    input_field_frame = Frame(root)
    input_field_frame.pack()
    button_frame = Frame(root)
    button_frame.pack()

    expression_input = Entry(input_field_frame, width=20)
    expression_input.pack()

    run_button = Button(button_frame, text="SOLVE")
    run_button.pack()
    run_button.bind("<Button-1>", solve)

    root.mainloop()
