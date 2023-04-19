import tkinter
from tkinter import ttk as tk
import config


class UserForm(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Widgets
        self.mainLabel = tk.Label(self)
        self.goBackButton = tk.Button(self)
        self.createButton = tk.Button(self)

        # Sub frames
        self.userInfoFrame = tk.LabelFrame(self)
        self.categoryInfoFrame = tk.LabelFrame(self)

        # individual form components
        self.nameLabel = tk.Label(self.userInfoFrame)
        self.nameEntry = tk.Entry(self.userInfoFrame)

        self.lastNameLabel = tk.Label(self.userInfoFrame)
        self.lastNameEntry = tk.Entry(self.userInfoFrame)

        self.secondLastNameLabel = tk.Label(self.userInfoFrame)
        self.secondLastNameEntry = tk.Entry(self.userInfoFrame)

        self.curpLabel = tk.Label(self.userInfoFrame)
        self.curpEntry = tk.Entry(self.userInfoFrame)

        self.ageLabel = tk.Label(self.userInfoFrame)
        self.ageEntry = tk.Entry(self.userInfoFrame)

        self.genderLabel = tk.Label(self.userInfoFrame)
        self.genderComboBox = tk.Combobox(self.userInfoFrame)

        self.addressLabel = tk.Label(self.userInfoFrame)
        self.addressEntry = tk.Entry(self.userInfoFrame)

        self.schoolLabel = tk.Label(self.userInfoFrame)
        self.schoolEntry = tk.Entry(self.userInfoFrame)

        self.categoryLabel = tk.Label(self.categoryInfoFrame)
        self.categoryComboBox = tk.Combobox(self.categoryInfoFrame)

        self.priceLabel = tk.Label(self.categoryInfoFrame)

        self.widgetsConfig()

    def widgetsConfig(self):
        self.mainLabel.configure(
            text="User form", font=("forest-dark", 30, "bold"))

        self.goBackButton.configure(
            text="Go back", command=lambda: self.master.showFrame("Dashboard"))

        self.nameLabel.configure(text="First name*")

        self.lastNameLabel.configure(text="Last name*")

        self.secondLastNameLabel.configure(text="Second last name")

        self.ageLabel.configure(text="Age*")
        validate = self.register(self.validateAge)
        self.ageEntry.configure(validate="key", validatecommand=(
            validate, "%S"))

        self.curpLabel.configure(text="Curp*")

        self.genderLabel.configure(text="Gender*")
        self.genderComboBox.configure(
            values=["Male", "Female"])

        self.addressLabel.configure(text="Address*")

        self.schoolLabel.configure(text="School*")

        self.render()
        return

    def render(self):
        # User info sub-frame
        self.nameLabel.grid(column=0, row=0)
        self.lastNameLabel.grid(column=1, row=0)
        self.secondLastNameLabel.grid(column=2, row=0)
        self.nameEntry.grid(column=0, row=1)
        self.lastNameEntry.grid(column=1, row=1)
        self.secondLastNameEntry.grid(column=2, row=1)

        self.ageLabel.grid(column=0, row=2)
        self.curpLabel.grid(column=2, row=2)
        self.ageEntry.grid(column=0, row=3)
        self.curpEntry.grid(column=2, row=3)

        for widget in self.userInfoFrame.winfo_children():
            widget.grid_configure(padx=3, pady=3)

        self.mainLabel.pack()
        self.userInfoFrame.pack(ipadx=50, padx=10, pady=10)
        self.categoryInfoFrame.pack()
        self.goBackButton.pack()
        return

    def validateAge(self, text: str):
        return text.isdigit() or text == ""
