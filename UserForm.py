import tkinter
from tkinter import ttk as tk


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
        self.categoryComboBox.bind(
            "<<ComboboxSelected>>", self.onCategorySelection)

        self.priceLabel = tk.Label(self.categoryInfoFrame)

        self.price = tkinter.StringVar()
        self.price.set("Category not selected")

        self.widgetsConfig()

    def widgetsConfig(self):
        self.userInfoFrame.configure(text="User information")
        self.categoryInfoFrame.configure(text="Category information")

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

        self.categoryLabel.configure(text="Category*")

        self.categoryComboBox.configure(
            values=["Advanced", "Intermediate", "Novice"])

        self.priceLabel.configure(
            font=("forest-dark", 13, "bold"), textvariable=self.price)

        self.render()
        return

    def pack(self, **kargs):
        self.onFocus()
        super().pack(**kargs)

    def onFocus(self):
        print('Se hizo focus al userForm')
        return

    def render(self):
        # User info sub-frame
        self.nameLabel.grid(column=0, row=0)
        self.nameEntry.grid(column=0, row=1)

        self.lastNameLabel.grid(column=1, row=0)
        self.lastNameEntry.grid(column=1, row=1)

        self.secondLastNameLabel.grid(column=2, row=0)
        self.secondLastNameEntry.grid(column=2, row=1)

        self.ageLabel.grid(column=0, row=2)
        self.ageEntry.grid(column=0, row=3)

        self.curpLabel.grid(column=1, row=2)
        self.curpEntry.grid(column=1, row=3)

        self.genderLabel.grid(column=2, row=2)
        self.genderComboBox.grid(column=2, row=3)

        self.addressLabel.grid(column=0, row=4)
        self.addressEntry.grid(column=0, row=5)

        self.schoolLabel.grid(column=2, row=4)
        self.schoolEntry.grid(column=2, row=5)

        for widget in self.userInfoFrame.winfo_children():
            widget.grid_configure(padx=3, pady=3)

        self.categoryLabel.grid(column=0, row=0)
        self.categoryComboBox.grid(column=0, row=1)

        self.priceLabel.grid(column=1, row=1)

        for widget in self.categoryInfoFrame.winfo_children():
            widget.grid_configure(padx=5)

        self.mainLabel.pack()
        self.userInfoFrame.pack(ipadx=50, ipady=7, padx=10, pady=10)
        self.categoryInfoFrame.pack(ipadx=50, ipady=7, padx=10, pady=10)
        self.goBackButton.pack()
        return

    def validateAge(self, text: str):
        return text.isdigit() or text == ""

    def onCategorySelection(self, e):
        actions = {
            "Advanced": lambda: self.price.set("500.00 MXN"),
            "Intermediate": lambda: self.price.set("350.00 MXN"),
            "Novice": lambda: self.price.set("250.00 MXN")
        }

        actions.get(self.categoryComboBox.get())()
        return
