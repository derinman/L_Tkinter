# ch19_20_10.py
from tkinter import * 
import math

class Circle:
    def __init__(self, x, y, r):
        ''' x,y坐標軸, r半徑 '''
        self.x = x
        self.y = y
        self.r = r    
    def setX(self, x):
        self.x = x        
    def setY(self, y):
        self.y = y 
    def is_insides(self, x, y):
        d = distance(x, y, self.x, self.y)
        return d <= self.r  
    def is_overlap(self, circle):
        d = distance(self.x, self.y, circle.x, circle.y)
        return  d <= self.r + circle.r
            
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
def show_Circle(c, obj):
    canvas.delete(obj)
    canvas.create_oval(c.x-c.r,c.y-c.r,c.x+c.r,c.y+c.r,tags=obj,fill='yellow')
    canvas.create_text(c.x, c.y, text=obj, tags=obj)           
def draged(event):
    '''拖曳移動圓'''
    if c1.is_insides(event.x, event.y):
        c1.setX(event.x)
        c1.setY(event.y)
        show_Circle(c1, "c1")
        if c1.is_overlap(c2):
            label["text"] = "兩圓相交或重疊"
        else:
            label["text"] = "兩圓沒有相交或重疊"
    elif c2.is_insides(event.x, event.y):
        c2.setX(event.x)
        c2.setY(event.y)
        show_Circle(c2, "c2")
        if c1.is_overlap(c2):
            label["text"] = "兩圓相交或重疊"
        else:
            label["text"] = "兩圓沒有相交或重疊"
            
window = Tk() 
window.title("ch19_20_10") 

wd = 400
ht = 300
label = Label(window, text = "兩圓相交或重疊" )
label.pack()
canvas = Canvas(window, width=wd, height=ht)
canvas.pack()

canvas.bind("<B1-Motion>", draged)
c1 = Circle(wd/2, ht/3, 30)
c2 = Circle(wd/2, ht*2/3, 50)
show_Circle(c1, "c1")
show_Circle(c2, "c2")

window.mainloop() 
