import tkinter
from tkinter import messagebox
from tkinter import ttk as tk
from Cursor import Cursor
from Document import Document


class UserForm(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.tempContender = None
        self.docMaker = Document()
        self.createButtonText = tkinter.StringVar()

        # Sub frames
        self.userInfoFrame = tk.LabelFrame(self)
        self.categoryInfoFrame = tk.LabelFrame(self)
        self.buttonsFrame = tk.Frame(self)

        # Widgets
        self.mainLabel = tk.Label(self)
        self.goBackButton = tk.Button(self.buttonsFrame)
        self.createButton = tk.Button(self.buttonsFrame)
        self.deleteButton = tk.Button(self.buttonsFrame)

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

        self.cursor = Cursor()

        self.widgetsConfig()

    # Config
    def widgetsConfig(self):
        self.userInfoFrame.configure(text="User information")
        self.categoryInfoFrame.configure(text="Category information")

        self.mainLabel.configure(
            text="User form", font=("forest-dark", 30, "bold"))

        self.goBackButton.configure(
            text="Go back", command=self.onBlur)

        self.createButton.configure(
            textvariable=self.createButtonText, command=self.dispatchContender)

        self.deleteButton.configure(
            text="Delete", command=self.deleteContender)

        self.nameLabel.configure(text="First name*")

        self.lastNameLabel.configure(text="Last name*")

        self.secondLastNameLabel.configure(text="Second last name")

        self.ageLabel.configure(text="Age*")
        ageValidation = self.register(self.validateAge)
        self.ageEntry.configure(validate="key", validatecommand=(
            ageValidation, "%P"))

        self.curpLabel.configure(text="Curp*")
        self.curpValidation = self.register(self.validateCurp)
        self.curpEntry.configure(
            validate="key", validatecommand=(self.curpValidation, "%P"))

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

    # Queries
    def dispatchContender(self):
        contender = {
            "name": self.nameEntry.get(),
            "firstLastName": self.lastNameEntry.get(),
            "secondLastName": self.secondLastNameEntry.get(),
            "age": self.ageEntry.get(),
            "curp": self.curpEntry.get(),
            "gender": self.genderComboBox.get(),
            "address": self.addressEntry.get(),
            "school": self.schoolEntry.get(),
            "category": self.categoryComboBox.get(),
            "payment": self.price.get(),
        }
        response = None
        message = ""
        if (self.tempContender is None):
            response = self.cursor.addContender(contender=contender)
            self.docMaker.createTicket(contender=contender)
            self.docMaker.createAppreciationCertificate(contender=contender)
            message = "Contender added!"
        else:
            response = self.cursor.updateContender(
                contender=contender, id=self.tempContender[0])
            message = "Contender updated!"

        if (response):
            messagebox.showinfo(message=message)
            self.nameEntry.delete(0, "end")
            self.lastNameEntry.delete(0, "end")
            self.secondLastNameEntry.delete(0, "end")
            self.ageEntry.delete(0, "end")
            self.curpEntry.delete(0, "end")
            self.genderComboBox.delete(0, "end")
            self.addressEntry.delete(0, "end")
            self.schoolEntry.delete(0, "end")
            self.categoryComboBox.delete(0, "end")
            self.price.set("Category not selected")
            self.master.showFrame("Dashboard")
        else:
            messagebox.showerror(message="There was an error!")

        return

    def deleteContender(self):
        id = self.tempContender[0]
        response = self.cursor.deleteContender(id)
        if (response):
            messagebox.showinfo(message="Contender deleted")
            self.onBlur()
        else:
            messagebox.showinfo(message="An error ocurred!")

    #  Validations

    def validateAge(self, text: str):
        if len(text) <= 2:
            return text.isdigit() or text == ""
        else:
            return False

    def validateCurp(self, text: str):
        return len(text) <= 18

    def onCategorySelection(self, e):
        actions = {
            "Advanced": lambda: self.price.set("500.00 MXN"),
            "Intermediate": lambda: self.price.set("350.00 MXN"),
            "Novice": lambda: self.price.set("250.00 MXN")
        }

        actions.get(self.categoryComboBox.get())()
        return

    # Render functions
    def onBlur(self):
        self.nameEntry.delete(0, "end")
        self.lastNameEntry.delete(0, "end")
        self.secondLastNameEntry.delete(0, "end")
        self.ageEntry.delete(0, "end")
        self.curpEntry.delete(0, "end")
        self.genderComboBox.delete(0, "end")
        self.addressEntry.delete(0, "end")
        self.schoolEntry.delete(0, "end")
        self.categoryComboBox.delete(0, "end")
        self.price.set("Category not selected")
        self.tempContender = None
        self.master.showFrame("Dashboard")
        return

    def pack(self, **kargs):
        self.onFocus()
        super().pack(**kargs)

    def onFocus(self):
        if (self.tempContender is None):
            self.createButtonText.set("Add")
            self.deleteButton.grid_forget()
            return

        self.createButtonText.set("Update")
        self.deleteButton.grid(column=3, row=0, padx=5)
        nameArr = self.tempContender[1].split()
        self.nameEntry.insert(0, nameArr[0])
        self.lastNameEntry.insert(0, nameArr[1])
        self.secondLastNameEntry.insert(0, nameArr[2])
        self.ageEntry.insert(0, self.tempContender[2])
        self.curpEntry.insert(0, self.tempContender[3])
        self.genderComboBox.insert(0, self.tempContender[4])
        self.addressEntry.insert(0, self.tempContender[5])
        self.schoolEntry.insert(0, self.tempContender[6])
        self.categoryComboBox.insert(0, self.tempContender[7])
        self.price.set(f"{self.tempContender[8]}0 MXN")
        return

    def render(self):
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

        self.goBackButton.grid(column=0, row=0, padx=5)
        self.createButton.grid(column=1, row=0, padx=5)

        self.mainLabel.pack()
        self.userInfoFrame.pack(ipadx=50, ipady=7, padx=10, pady=10)
        self.categoryInfoFrame.pack(ipadx=50, ipady=7, padx=10, pady=10)
        self.buttonsFrame.pack()
        return
