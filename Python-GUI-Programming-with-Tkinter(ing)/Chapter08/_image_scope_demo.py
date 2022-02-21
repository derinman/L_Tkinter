import tkinter as tk

from pathlib import Path


script_location = Path(__file__).absolute().parent

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        tk.Label(self, image=tk.PhotoImage(file=script_location/'smile.gif')).pack()
        smile = tk.PhotoImage(file=script_location/'smile.gif')
        tk.Label(self, image=smile).pack()
        self.smile = tk.PhotoImage(file=script_location/'smile.gif')
        tk.Label(self, image=self.smile).pack()

App().mainloop()
