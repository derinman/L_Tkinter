# ch6_6.py
from tkinter import *

# x = StringVar() # 儲存一個 string 型別變數, 預設值為""
# x = IntVar() # 儲存一個整型變數, 預設值為0
# x = DoubleVar() # 儲存一個浮點型變數, 預設值為0.0
# x = BooleanVar() # 儲存一個布林型變數, 返回值為 0 (代表 False) 或 1 (代表 True)

def callbackW(name,index,mode):         # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容
    print("name = %r, index = %r, mode = %r" % (name,index,mode)) 

root = Tk()
root.title("ch6_5")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容
xE.trace("w",callbackW)                 # 若是有更改執行callbackW

entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

root.mainloop()






