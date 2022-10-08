# ch3_39.py
from tkinter import *

import os 

dirname = os.path.dirname(__file__)

root = Tk()
root.title("ch3_39")
root.geometry("640x480")

night = PhotoImage(file=dirname+"/night.png")
label=Label(root,image=night)
label.place(relx=0.1,rely=0.1,relheight=0.8)

root.mainloop()




