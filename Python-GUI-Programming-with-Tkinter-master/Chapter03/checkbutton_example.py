import tkinter as tk
from tkinter import ttk

parent = tk.Tk()
my_boolean_var = tk.BooleanVar()

def print_result():
    print('click')

my_checkbutton = ttk.Checkbutton(
    text="Check to make this option True",
    variable=my_boolean_var,
    command=print_result
)



my_checkbutton.pack()
parent.mainloop()
