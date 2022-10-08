# ch6_4.py
from tkinter import *

# x = StringVar() # 儲存一個 string 型別變數, 預設值為""
# x = IntVar() # 儲存一個整型變數, 預設值為0
# x = DoubleVar() # 儲存一個浮點型變數, 預設值為0.0
# x = BooleanVar() # 儲存一個布林型變數, 返回值為 0 (代表 False) 或 1 (代表 True)

def callback(*args):
    xL.set(xE.get())                    # 更改標籤內容
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
root = Tk()
root.title("ch6_4")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容
entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)   

root.mainloop()






