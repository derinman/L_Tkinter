# ch4_9.py
from tkinter import *

import os

dirname = os.path.dirname(__file__)

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_9")                                  # 視窗標題
label = Label(root)                                 # 標籤內容

sunGif = PhotoImage(file=dirname+"/sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=LEFT)          
label.pack()                      
btn.pack()

root.mainloop()






