context_menu = tk.Menu(win)
context_menu.add_command(label='close', command=win.destroy)

def on_right_click(event):
    x = win.winfo_x() + event.x
    y = win.winfo_y() + event.y

    context_menu.post(x, y)

win.bind('<Button-3>', on_right_click)