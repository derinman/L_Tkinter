import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")

        label = tk.Label(self, text="Hello World!",bg='green')
        label.pack(fill=tk.BOTH, expand=0, padx=200, pady=50)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
        
