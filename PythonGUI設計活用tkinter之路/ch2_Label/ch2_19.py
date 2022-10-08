# ch2_19.py
from tkinter import *

import os
dirname = os.path.dirname(__file__)


root = Tk()
root.title("ch2_19")

html_gif = PhotoImage(file=dirname+'/html.gif')
label=Label(root,image=html_gif)
label.pack()

root.mainloop()




