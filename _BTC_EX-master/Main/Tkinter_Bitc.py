# Get from Sentdex visit SentDex channel on GitHub for more information
# This code comes from the video series of tkinter by SentDex
# visit
# https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ

import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import urllib
import json
import pandas as pd
import numpy as np
import os

print(os.getcwd())

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")


#amimation function
#live graph channel

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111) # means only one chart
sampledataPath = 'sampledata.txt'

def animate(i):
    pullData = open(sampledataPath, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    print(xList)
    a.clear()
    a.plot(xList,yList)

#style.use("dark_background")

class SeaofBTapp(tk.Tk): # is an inheritance not a parameter Tk class within tkinter

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs) #usually we do root=tk.Tk


        # img_path = "image/clienticon.ico"
        # photo = tk.PhotoImage(file=img_path)
        # self.tk.call("wm", "iconphoto", self._w, photo)

        self.title("Sea Of BTC client")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {} # insieme di tutti i frame

        for F in (StartPage, BTCe_Page): ###AGGIUNGI QUI LE PAGINE *****
            frame = F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self,cont):

        frame = self.frames[cont] # cont is the key the value is grabbed in the dict
        frame.tkraise() #always on top  we can use the method .tkraise becuase we inherited tk.Tk

class StartPage(tk.Frame):  # sono obbligato a fare una classe perchè deve ereditare tk.Frame

    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=""" ALPHA bitcoin trading application 
        use at your own risk there is no promise of warranty
        """, font= LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree", command= lambda: controller.show_frame(BTCe_Page))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree", command= quit)
        button2.pack()



class PageOne(tk.Frame):  # sono obbligato a fare una classe perchè deve ereditare tk.Frame

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)   # questo non ho capito perché devo farlo
        label = ttk.Label(self, text="Page One", font= LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Start Page", command= lambda: controller.show_frame(StartPage))
        button1.pack()



class BTCe_Page(tk.Frame):  # sono obbligato a fare una classe perchè deve ereditare tk.Frame

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)   # questo non ho capito perché devo farlo
        label = ttk.Label(self, text="BTCe_Page", font= LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command= lambda: controller.show_frame(StartPage))
        button1.pack()

        # f = Figure(figsize=(5,5), dpi=100)
        # a = f.add_subplot(111) # means only one chart
        # a.plot([1,2,3,4,5,6,7,8],[5,6,8,4,2,3,7,1])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()    #corretto da SentDex canvas.show() aggiornamento
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #we add navigation bar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTapp() # it's like to do app= tk.TK()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()









