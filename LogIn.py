import tkinter
from tkinter import messagebox
from tkinter import ttk as tk
from PIL import Image, ImageTk
from Cursor import Cursor


class LogIn(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.mainLabel = tk.Label(self)
        self.emailEntry = customEntry(self, "Email", False)
        self.passwordEntry = customEntry(self, "Password", True)
        self.submitButton = tk.Button(self)
        self.image = Image.open("assets/logo.png")
        self.image = self.image.resize((150, 150))
        self.imagePI = ImageTk.PhotoImage(self.image)
        self.imageLabel = tk.Label(self)
        self.cursor = Cursor()

        self.widgetsConfig()

    def widgetsConfig(self):
        self.imageLabel.configure(image=self.imagePI)

        self.mainLabel.configure(
            text="User login", font=("forest-dark", 30, "bold"))

        self.emailEntry.configure(width=25)

        self.passwordEntry.configure(width=25)

        self.submitButton.configure(
            width=20, text="Log in", command=self.logIn)
        self.render()
        return

    def logIn(self):
        # credentials = {
        #     "email": self.emailEntry.get(),
        #     "password": self.passwordEntry.get()
        # }
        # response = self.cursor.logIn(credentials=credentials)
        # if response:
        #     self.emailEntry.delete(0, "end")
        #     self.passwordEntry.delete(0, "end")
        #     self.emailEntry.insert(0, self.emailEntry.placeHolder)
        #     self.passwordEntry.insert(0, self.passwordEntry.placeHolder)
        #     self.passwordEntry.configure(show="")
        self.master.showFrame("Dashboard")
        # else:
        #     messagebox.showerror(message="The email or password is wrong")
        return

    def render(self):
        self.imageLabel.grid(column=0, row=0, columnspan=2)
        self.mainLabel.grid(column=0, row=1, columnspan=2)
        self.emailEntry.grid(column=1, row=2, pady=10)
        self.passwordEntry.grid(column=1, row=3, pady=10)
        self.submitButton.grid(column=0, row=4, columnspan=2, pady=5)
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
