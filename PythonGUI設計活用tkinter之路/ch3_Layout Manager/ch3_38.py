# ch3_38.py
from tkinter import *

import os

dirname = os.path.dirname(__file__)

root = Tk()
root.title("ch3_38")
root.geometry("640x480")

night = PhotoImage(file=dirname+"/night.png")
label=Label(root,image=night)
label.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

root.mainloop()




