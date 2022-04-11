# ch11_8.py
from tkinter import *
def btnClicked1():                  # Button按鈕事件處理程式1
    print("Command event handler, I like tkinter")
def btnClicked2(event):             # Button按鈕事件處理程式2
    print("Bind event handler, I like tkinter", event)
    
root = Tk()
root.title("ch11_8")                # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

btn = Button(root,text="tkinter",   # 建立按鈕tkinter
             command=btnClicked1)
btn.pack(anchor=W,padx=10,pady=10)
btn.bind("<Button-1>",btnClicked2, add='+')  # 增加事件處理程式
btn.bind("<Button-1>",lambda a: print(str(a)+'haha'), add='+')  #試著把add arg改掉就會無效,因為他們都綁定<Button-1>

# If you don’t specify the add='+' argument, the bind() method will replace the existing handler by the new one.

root.mainloop()








