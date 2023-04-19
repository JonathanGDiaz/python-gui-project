import tkinter as tk
from tkinter import ttk
from LogIn import LogIn


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = ttk.Style(self)
        self.tk.call("source", "forest-dark.tcl")
        self.style.theme_use("forest-dark")
        self.geometry("500x500")
        self.title("Chess tournament")

        # Frames
        self.logIn = LogIn(self)
        self.logIn.place(relx=0.5, rely=0.5, anchor="center")

        # self.logIn.grid(row=0, column=0, sticky="nsew")

        # First frame
        self.show_frame(self.logIn)

    def show_frame(self, frame):
        frame.tkraise()
