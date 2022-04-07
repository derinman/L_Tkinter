# ch19_12_1.py
from tkinter import *

def inside_circle(xCenter, yCenter, radius, x, y):
    distance = ((xCenter-x) * (xCenter-x) + (yCenter-y) * (yCenter-y)) ** 0.5;
    if distance <= radius:
        return True
    else:
        return False
def is_inside(event):
    canvas.delete("text")
    if inside_circle(wd/2, ht/2, r, event.x, event.y):
        canvas.create_text(event.x, event.y - 5, 
                           text="滑鼠游標在圓內", tags="text")
    else:
        canvas.create_text(event.x, event.y - 5, 
                           text="滑鼠游標在圓外", tags="text")

wd = 300                # 視窗寬度
ht = 240                # 視窗高度
r = 100                 # 圓半徑

window = Tk() 
window.title("ch19_12_1") 
        
canvas = Canvas(window, bg="yellow", width=wd, height=ht)
canvas.pack()
canvas.create_oval(wd/2 - r, ht/2 - r, wd/2 + r, ht/2 + r, tags = "circle")       
canvas.bind("<B1-Motion>", is_inside)
        
window.mainloop() 
        
   
