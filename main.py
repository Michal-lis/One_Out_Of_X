import tkinter as tk

from pages import PageOne, StartPage, PlayerSetupPage
from utils import restore_all_questions


class OneOfX(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="images/logo.ico")
        tk.Tk.wm_title(self, "1 out of X")
        self.geometry("600x630")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PlayerSetupPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# restore_all_questions()
app = OneOfX()
app.mainloop()
