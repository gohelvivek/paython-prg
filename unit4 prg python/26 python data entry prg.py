import tkinter as tk
from tkinter import simpledialog
application_window: tk.Tk = tk.Tk()
answer = simpledialog.askstring("input","what is your first name?",parent = application_window)
if answer is not None:
    ("Your first name is",answer)
else:
    ("You don't have a first name?")
answer = simpledialog.askinteger("input","What is your age?",parent = application_window, minvalue=0, maxvalue=100)
if answer is not None:
    ("Your age is",answer)
else:
    ("You don't have an age?")
answer = simpledialog.askfloat("input","What is your salary?", parent = application_window, minvalue = 0.0, maxvalue = 100000.0)
if answer is not None:
    ("Your salary is",answer)
else:
    ("You don't have a salary?")
