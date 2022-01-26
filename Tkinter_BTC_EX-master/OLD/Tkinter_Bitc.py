import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class SeaofBTapp(tk.Tk): # is an inheritance not a parameter Tk class within tkinter

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs) #usually we do root=tk.Tk

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # insieme di tutti i frame

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky='nsew')

        # frame = StartPage(container, self)
        # # DEF StartPage  -> creo nome frame associato a una funzione di lancio frame
        # # Non serve a un cazz mettere anche self che viene passato come controller...
        #
        # frame2 = PageOne (container, self)
        #
        # self.frames[StartPage] = frame      # inserisco nel dict di tutti i frame
        # #inserisco il grid nel DICT prima di fare il pack o il grid
        #
        # self.frames[PageOne] =frame2
        #
        # frame.grid(row=0, columns=1, sticky="nsew")
        # frame2.grid(row=0, columns=1, sticky="nsew")

        self.show_frame(StartPage)
        # DEF show_frame --> Porta in primo piano il Frame passato ()
        # Il frame passato lo va a recuperare dal dict self.frames{}
        # StartPage is the frame we want to show
        # ma StartPage is not a frame is a Class!!!!

    def show_frame(self,cont):

        frame = self.frames[cont] # cont is the key the value is grabbed in the dict
        # for example if the key is Start Page the frame = value --> StartPage(...)
        frame.tkraise() #always on top  we can use the method .tkraise becuase we inherited tk.Tk

class StartPage(tk.Frame):  # sono obbligato a fare una classe perchè deve ereditare tk.Frame

    def __init__(self, parent, controller):
        # self --> tk.Frame
        # parent --> ovvero il frame madre gli e lo passo con "container"
        # controller --> gli passo self ovvero SeaofBTapp quindi tk.Tk
        # prova a sostituire controller con tk.Tk e fargli ereditare tk.Tk
        tk.Frame.__init__(self, parent)   # questo non ho capito perché devo farlo
        label = ttk.Label(self, text="start page", font= LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit page1", command= lambda: controller.show_frame(PageOne))
        # gli passo PageOne come cont alla DEF show_frame che va a sua volta va a cercare PageOne
        # nel Dict frames quindi devo aggiungere nel dict questo frame
        button1.pack()

class PageOne(tk.Frame):  # sono obbligato a fare una classe perchè deve ereditare tk.Frame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   # questo non ho capito perché devo farlo
        label = ttk.Label(self, text="page One", font= LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Start Page", command= lambda: controller.show_frame(StartPage))
        button1.pack()

app = SeaofBTapp() # it's like to do app= tk.TK()
app.mainloop()









