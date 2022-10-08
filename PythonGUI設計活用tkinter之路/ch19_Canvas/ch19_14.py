# ch19_14.py
from tkinter import *
from PIL import Image, ImageTk

import os

dirname = os.path.dirname(__file__)

tk = Tk()
img = Image.open(dirname+"/rushmore.jpg")
rushMore = ImageTk.PhotoImage(img)

canvas = Canvas(tk, width=img.size[0]+40,
                height=img.size[1]+30)
canvas.create_image(20,15,anchor=NW,image=rushMore)
canvas.pack(fill=BOTH,expand=True)

tk.mainloop()











