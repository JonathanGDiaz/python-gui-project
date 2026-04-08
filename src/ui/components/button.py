from tkinter import ttk as tk

class CustomEntry(tk.Entry):
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
