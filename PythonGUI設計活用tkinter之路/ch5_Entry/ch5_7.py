# ch5_7.py
from tkinter import *

import os

dirname = os.path.dirname(__file__)

def printInfo():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    accountE.delete(0,END)              # 刪除account文字方塊的帳號內容
    pwdE.delete(0,END)                  # 刪除pwd文字方塊的密碼內容
    
root = Tk()
root.title("ch5_7")                     # 視窗標題

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file=dirname+"/sse.gif")     # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)

accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=1)

pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=2)

accountE = Entry(root)                  # 文字方塊account
accountE.insert(1,"Kevin")              # 預設Account內容
accountE.grid(row=1,column=1)           # 定位文字方塊accou


pwdE = Entry(root,show="*")             # 文字方塊pwd
pwdE.insert(1,"pwd")                    # 預設pwd內容
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd

# 以下建立Login和Quit案鈕
loginbtn = Button(root,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0,sticky=W,pady=5)

quitbtn = Button(root,text="Quit",command=root.quit)
quitbtn.grid(row=3,column=1,sticky=W,pady=5)

root.mainloop()






