# ch3_12.py
from tkinter import *

root = Tk()
root.title("ch3_12")
root.geometry("300x180")            # 設定視窗勘寬300高180
oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10

root.mainloop()




