from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class StartPage(Frame):
    def __init__(self, master, parent):
        # master is always the Tk isinstance
        # parent is the Frame instance named container
        Frame.__init__(self, master, parent)
        self.master = master

        # labels
        label = Label(self, text="Welcome to '1 z 10'!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # buttons
        button1 = ttk.Button(self, text="Let the game begin!", command=lambda: exit())
        button1.pack()

        # menus
        menu = Menu(self.master)
        self.master.config(menu=menu)
        menu.add_cascade(label='Exit', command=lambda: exit())

        # picutures
        # load = Image.open('images/tad_sznuk.jpg')
        # render = ImageTk.PhotoImage(load)
        # img = Label(self, image=render)
        # img.image = render
        # img.place(x=0, y=0)
