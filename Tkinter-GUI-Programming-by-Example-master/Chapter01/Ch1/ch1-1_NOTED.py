import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")

        label = tk.Label(self, text="Hello World!222",bg='green')
        label.pack(fill=tk.BOTH, padx=200, pady=200)
        # 上面 fill= 選項是如果將視窗拖放時候，自動將控制元件在 x 和 y 方向上填充。

if __name__ == "__main__":
    window = Window()
    window.mainloop()
        
