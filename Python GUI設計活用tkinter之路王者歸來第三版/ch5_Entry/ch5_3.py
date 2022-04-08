# ch5_3.py
from tkinter import *

import os

dirname = os.path.dirname(__file__)

root = Tk()
root.title("ch5_3")                     # 視窗標題

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file=dirname+"/sse.gif")     # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)

accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=1)

pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=2)


accountE = Entry(root)                  # 文字方塊account
accountE.grid(row=1,column=1)           # 定位文字方塊account

pwdE = Entry(root,show="*")             # 文字方塊pwd
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd

root.mainloop()






