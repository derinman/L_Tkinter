import tkinter as tk

root = tk.Tk()

def enter(event):
    print ('Entered Frame: x=%d, y=%d' % (event.x, event.y))

frame = tk.Frame(root, width=150, height=150)
frame.bind('<Any-Enter>', enter)
frame.pack()

root.mainloop()
