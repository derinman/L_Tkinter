import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class SeaofBTapp(tk.Tk): # is an inheritance not a parameter Tk class within tkinter

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs) #usually we do root=tk.Tk

        self.frame= StartPage(self)

class StartPage(tk.Frame):

    def __init__(self, pagina):

        tk.Frame.__init__(self)

        self.label1 = ttk.Label(self, text="ciao")
        self.label1.pack()


app = SeaofBTapp() # it's like to do app= tk.TK()
app.mainloop()