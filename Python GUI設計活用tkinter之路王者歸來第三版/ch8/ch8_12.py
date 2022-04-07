# ch8_12.py
from tkinter import * 

def click_Radiobutton():
    print(("淺藍色" if v1.get() == 1 else "淺綠色") 
          + "設定" )
    
def click_bold_box():
    print("粗體鈕 " 
          + ("設定" if v2.get() == 1 else "取消設定"))

def click_italic_box():
    print("斜體鈕 " 
          + ("設定" if v3.get() == 1 else "取消設定"))    
            
def get_Name():
    print("姓名 : " + name.get())

window = Tk() 
window.title("ch8_12")                          # 設定標題
       
# 在框架frame1,建立2個選項鈕和2個核對方塊
frame1 = Frame(window)                          # 建立框架frame1 
frame1.pack()      

v1 = IntVar()
v1.set(1)
rb_blue = Radiobutton(frame1, text="淺藍",
                      bg="lightblue", variable=v1, value=1, 
                      command=click_Radiobutton)
rb_green = Radiobutton(frame1, text="淺綠", 
                       bg="lightgreen", variable=v1, value=2, 
                       command=click_Radiobutton)
v2 = IntVar()
cbtBold = Checkbutton(frame1, text="粗體", 
                      variable=v2, command=click_bold_box)
v3 = IntVar()
cbtItalic = Checkbutton(frame1, text="斜體", 
                      variable=v3, command=click_italic_box)

rb_blue.grid(row = 1, column = 1)
rb_green.grid(row = 1, column = 2)
cbtBold.grid(row = 2,column = 1)
cbtItalic.grid(row = 2,column = 2)
       
# 在框架frame2,建立1個標籤和1個文字方塊
frame2 = Frame(window)                          # 建立框架frame2 
frame2.pack()
label = Label(frame2, text="請輸入名字: ")
name = StringVar()
name_Entry = Entry(frame2, textvariable=name) 
name_Btn = Button(frame2, text="執行", command=get_Name)

label.grid(row=1, column=1)
name_Entry.grid(row=1, column=2)
name_Btn.grid(row=1, column=3, padx=3)
        
# 輸出文字
lbl = Label(window,text="控件組合應用")           # 輸出文字
lbl.pack()
        
window.mainloop() 




