from tkinter import *
from PIL import Image, ImageTk

# created by mlis 30.01.2018
# modules used pillow,tkinter

LARGE_FONT = ("Verdana", 12)


class TopLevelWidget(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # container is a frame containting all the other fremes
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # minimum size, priority
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        frame.pack()

        self.frames[StartPage] = frame
        self.show_frame(StartPage)

    def show_frame(self, frame_key):
        frame = self.frames[frame_key]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="Visit Page 1", command=lambda: exit())
        button1.pack()


root = TopLevelWidget()
root.mainloop()
