# ch6_2.py
from tkinter import *

# x = StringVar() # 儲存一個 string 型別變數, 預設值為""
# x = IntVar() # 儲存一個整型變數, 預設值為0
# x = DoubleVar() # 儲存一個浮點型變數, 預設值為0.0
# x = BooleanVar() # 儲存一個布林型變數, 返回值為 0 (代表 False) 或 1 (代表 True)

def btn_hit():                      # 處理按鈕事件
    if x.get() == "":               # 如果目前是空字串
        x.set("I like tkinter")     # 顯示文字
    else:
        x.set("")                   # 不顯示文字
   
root = Tk()
root.title("ch6_2")                 # 視窗標題
    
x = StringVar()                     # Label的變數內容

label = Label(root,textvariable=x,          # 設定Label內容是變數x
              fg="blue",bg="lightyellow",   # 淺黃色底藍色字
              font="Verdana 16 bold",       # 字型設定
              width=25,height=2)            # 標籤內容
label.pack()   
btn = Button(root,text="Click Me",command=btn_hit)
btn.pack()                   

root.mainloop()






