# ch7_8.py
from tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

root = Tk()
root.title("ch7_8")                         # 視窗標題

Label(root,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(root,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
btn = Button(root,text="確定",width=10,command=printInfo)
btn.grid(row=i+2)

root.mainloop()






