import tkinter as tk
from tkinter import ttk
import asyncio

class App:
    async def exec(self):
        self.window = Window()
        task1 = asyncio.create_task(self.window.do_some())
        task2 = asyncio.create_task(self.window.loading())
        await task1
        await task2

class Window(tk.Tk):
    def __init__(self):
        self.root = tk.Tk()
        self.animation = "░▒▒▒▒▒"
        self.label = tk.Label(text="")
        self.label.grid(row=0, columnspan=2, padx=(8, 8), pady=(16, 0))
        self.pb = ttk.Progressbar(length=280)
        self.pb["maximum"] = 100
        self.pb["value"] = 0
        self.pb.grid(row=1, columnspan=2, padx=(8, 8), pady=(16, 0))

    async def do_some(self):
        while True:
            self.label["text"] = self.animation
            self.animation = self.animation[1:] + self.animation[0]
            self.root.update()
            await asyncio.sleep(.1)

    async def loading(self):
        while self.pb.cget("value") <= self.pb["maximum"]:
            self.pb.step(2)
            self.root.update()
            await asyncio.sleep(.1)

asyncio.run(App().exec())