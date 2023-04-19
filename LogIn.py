import tkinter
from tkinter import ttk as tk


class LogIn(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.mainLabel = tk.Label(self)
        self.emailEntry = customEntry(self, "Email", False)
        self.passwordEntry = customEntry(self, "Password", True)
        self.submitButton = tk.Button(self)

        self.widgetsConfig()

    def widgetsConfig(self):
        self.mainLabel.configure(
            text="User login", font=('forest-dark', 30, 'bold'))

        # Email configuration
        self.emailEntry.configure(width=25)

        # Password configuration
        self.passwordEntry.configure(width=25, show="\u2022")

        # Submit button
        self.submitButton.configure(
            width=20, text="Log in", command=lambda: self.master.showFrame("Dashboard"))
        self.render()
        return

    def render(self):
        self.mainLabel.grid(column=0, row=0, columnspan=2)
        self.emailEntry.grid(column=1, row=1, pady=10)
        self.passwordEntry.grid(column=1, row=2, pady=10)
        self.submitButton.grid(column=0, row=3, columnspan=2, pady=5)
        return


class customEntry(tk.Entry):
    def __init__(self, master, placeHolder, isPassword):
        super().__init__(master)
        self.placeHolder = placeHolder
        self.isPassword = isPassword
        self.insert(0, placeHolder)
        self.bind("<FocusIn>", self.deletePlaceHolder)
        self.bind("<FocusOut>", self.addPlaceHolder)
        return

    def deletePlaceHolder(self, e):
        if self.isPassword:
            self.configure(show="\u2022")

        if self.get() == self.placeHolder:
            self.delete(0, "end")
        return

    def addPlaceHolder(self, e):
        if not self.get():
            self.configure(show="")
            self.insert(0, self.placeHolder)
        return
