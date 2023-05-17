import tkinter as tk
from tkinter import ttk
from LogIn import LogIn
from Dashboard import Dashboard
from UserForm import UserForm
from Winners import Winners


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = ttk.Style(self)
        self.tk.call("source", "assets/forest-dark.tcl")
        self.style.theme_use("forest-dark")
        self.geometry("600x500")
        self.title("Chess tournament")
        self.frames = {}

        for F in (LogIn, Dashboard, UserForm, Winners):
            frame = F(self)
            self.frames[F.__name__] = frame

        self.showFrame("LogIn")
        return

    def showFrame(self, name: str):
        for frame in self.frames.values():
            frame.place_forget()
            frame.pack_forget()

        if isinstance(self.frames[name], LogIn):
            self.frames[name].place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.frames[name].pack(anchor=tk.CENTER)
