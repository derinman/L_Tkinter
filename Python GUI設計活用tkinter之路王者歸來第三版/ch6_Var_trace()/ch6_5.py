# ch6_5.py
from tkinter import *

# x = StringVar() # 儲存一個 string 型別變數, 預設值為""
# x = IntVar() # 儲存一個整型變數, 預設值為0
# x = DoubleVar() # 儲存一個浮點型變數, 預設值為0.0
# x = BooleanVar() # 儲存一個布林型變數, 返回值為 0 (代表 False) 或 1 (代表 True)

def callbackW(*args):                   # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容

def callbackR(*args):                   # 內容被讀取時執行
    print("Warning:資料被讀取!")

def hit():                              # 讀取資料
    print("讀取資料:",xE.get())
  
root = Tk()
root.title("ch6_5")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容
entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW
xE.trace("r",callbackR)                 # 若是有被讀取執行callbackR

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

btn = Button(root,text="讀取",command=hit)    # 建立讀取按鈕
btn.pack(pady=5)

root.mainloop()






