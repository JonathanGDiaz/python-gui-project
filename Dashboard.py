import tkinter as tk
from tkinter import ttk as tk


class Dashboard (tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.mainLabel = tk.Label(self)
        self.addButton = tk.Button(self)
        self.winnerButton = tk.Button(self)
        self.logoutButton = tk.Button(self)

        self.widgetsConfig()

    def widgetsConfig(self):
        self.mainLabel.configure(
            text="Welcome!", font=("forest-dark", 30, "bold"))

        self.addButton.configure(
            text="Add a contender", command=lambda: self.master.showFrame("UserForm"))

        self.winnerButton.configure(text="Choose winners")

        self.logoutButton.configure(
            text="Log out", command=lambda: self.master.showFrame("LogIn"))

        self.render()
        return

    def pack(self, **kargs):
        self.onFocus()
        super().pack(**kargs)

    def onFocus(self):
        print('Se hizo focus al dashBoard')
        return

    def render(self):
        self.mainLabel.grid(column=0, row=0, columnspan=5)
        self.logoutButton.grid(column=0, row=1, padx=10)
        self.addButton.grid(column=1, row=1, padx=10)
        self.winnerButton.grid(column=2, row=1, padx=10)
        return
