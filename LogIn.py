import tkinter as tk
import config


class LogIn(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.mainLabel = tk.Label(self)
        self.emailLabel = tk.Label(self)
        self.emailEntry = tk.Entry(self)
        self.passwordLabel = tk.Label(self)
        self.passwordEntry = tk.Entry(self)
        self.submitButton = tk.Button(self)

        self.widgetsConfig()

    def widgetsConfig(self):
        self.mainLabel.configure(
            text="Welcome!", font=('forest-dark', 30, 'bold'))

        # Email configuration
        self.emailLabel.configure(text="Email")
        self.emailEntry.configure(
            width=25, bg=config.customColors["EntryBG"], fg=config.customColors["EntryFG"])

        # Password configuration
        self.passwordLabel.configure(text="Password")
        self.passwordEntry.configure(
            width=25, show="*", bg=config.customColors["EntryBG"], fg=config.customColors["EntryFG"])

        # Submit button
        self.submitButton.configure(
            width=20, text="Log in")
        self.render()
        return

    def render(self):
        self.mainLabel.grid(column=0, row=0, columnspan=2)
        self.emailLabel.grid(column=0, row=1, pady=10)
        self.emailEntry.grid(column=1, row=1, pady=10)
        self.passwordLabel.grid(column=0, row=2, pady=10)
        self.passwordEntry.grid(column=1, row=2, pady=10)
        self.submitButton.grid(column=0, row=3, columnspan=2, pady=5)
        return
