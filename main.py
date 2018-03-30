from tkinter import *
from pages import StartPage

"""
created by mlis 30.01.2018
pypi modules used: pillow,tkinter
"""


class TopLevelWidget(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("1 z 10 - The Game")
        self.iconbitmap(self, default="images/logo.ico")

        self.init_global_container()

        page_list = [StartPage]
        self.init_pages(page_list)

        self.show_frame(StartPage)

    def init_pages(self, pages):
        for F in pages:
            frame = F(self, self.container)
            frame.pack()
            self.frames[F] = frame

    def init_global_container(self):
        # container is a frame containting all the other fremes
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # minimum size, priority
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.container = container
        self.frames = {}

    def show_frame(self, frame_key):
        frame = self.frames[frame_key]
        frame.tkraise()


root = TopLevelWidget()
root.mainloop()
