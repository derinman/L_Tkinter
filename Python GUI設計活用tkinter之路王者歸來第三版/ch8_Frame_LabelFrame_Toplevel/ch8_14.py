# ch8_14.py
from tkinter import * 
import random

import os

dirname = os.path.dirname(__file__)

def do_shuffle():
    random.shuffle(gifList)
    for i in range(3):
        labelList[i]["image"] = gifList[i]
      
window = Tk() 
window.title("ch8_14") 
        
gifList = []                    # 圖片串列
for i in range(1, 8):           # 建立圖片串列
    gifList.append(PhotoImage(file=dirname+"/bookfigures/" + str(i) + ".gif"))
        
frame = Frame(window)           # 容器, 儲存圖書封面
frame.pack()
        
labelList = []                  # 圖書封面串列
for i in range(3):
    labelList.append(Label(frame, image=gifList[i]))
    labelList[i].pack(side=LEFT)
        
Button(window, text="重新顯示", command=do_shuffle).pack(pady=5)
        
window.mainloop() 

   

        

