# ch19_20_8.py
from tkinter import * 
import math

def show_pendulum():
    global angle
    global step
    x1 = wd / 2;                    # 鐘擺中心x座標
    y1 = ht / 10;                   # 鐘擺中心y座標      
    if angle < right_Angle:
        step = 1                    # 向左擺盪
    elif angle > left_Angle:
        step = -1                   # 向右擺盪          
    angle += step
    x = x1 + pendulum_radius * math.cos(math.radians(angle))
    y = y1 + pendulum_radius * math.sin(math.radians(angle))          
    canvas.create_line(x1, y1, x, y, fill="goldenrod", tags = "pendulum")   # 鐘擺軸長條
    canvas.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, fill = "gold",       # 鐘擺軸心
                       outline = "gold", tags = "pendulum")
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius,      # 鐘擺球體
                       fill = "gold", outline = "gold", tags = "pendulum") 

wd = 300                            # 視窗寬
ht = 300                            # 視窗高
r = 2                               # 鐘擺軸心半徑
radius = 15                         # 鐘擺球體半徑
pendulum_radius = ht * 0.75

left_Angle = 120                    # 擺盪最左邊角度
right_Angle = 60                    # 擺盪最右邊角度
step = 1                            # 每次移動角度

window = Tk()                       
window.title("ch19_20_8")            
        
canvas = Canvas(window, bg="blue", width=wd, height=ht)
canvas.pack()

angle = left_Angle
delay = 50                          # 0.5秒
        
while True:
    canvas.delete("pendulum")
    show_pendulum()
    canvas.after(delay)               
    canvas.update()                 # 更新畫布

window.mainloop()                  

     


