import tkinter as tk
import os

from PIL import Image, ImageTk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


def start_game():
    os.system("python gameflow.py")


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""Welcome to the 1 of X Game. 
        My name is Tadeusz and I am the master of ceremony here. 
        Do you want to play?"""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        load = Image.open('images/tad_sznuk.jpg')
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=160)

        button1 = ttk.Button(self, text="Yes",
                             command=lambda: start_game())
        button1.pack(pady=2, padx=10)

        button2 = ttk.Button(self, text="No",
                             command=quit)
        button2.pack(pady=2, padx=10)


# FOR FUTURE FULL GUI
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PlayerSetupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Please give the names of players:", font=LARGE_FONT)
        label.grid(row=0, column=2)

        labels = []
        entries = []
        number_of_players = 7
        for n in range(number_of_players):
            labels.append(tk.Label(self, text="Player number {}: ".format(n + 1), font=LARGE_FONT))
            labels[n].grid(row=2 + n, column=2)
            entries.append(tk.Entry(self))
            entries[n].grid(row=2 + n, column=3)

        button1 = ttk.Button(self, text="Lets start the game!",
                             command=lambda: controller.show_frame(StartPage))
        button1.grid(row=number_of_players + 2, column=3)
