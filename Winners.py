import tkinter
from tkinter import ttk as tk
from Cursor import Cursor
from LogIn import customEntry
from Document import Document

class Winners (tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.filter = "Novice"
        self.cursor = Cursor()
        self.docMaker = Document()
        self.titleLabel = tk.Label(self)
        self.buttonFrame = tk.Frame(self)
        self.noviceButton = tk.Button(self.buttonFrame)
        self.intermediateButton = tk.Button(self.buttonFrame)
        self.advancedButton = tk.Button(self.buttonFrame)
        self.cancelButton = tk.Button(self.buttonFrame)
        self.treeFrame = tk.Frame(self)
        self.treeView = tk.Treeview(self.treeFrame)
        self.scrollbar = tk.Scrollbar(self.treeFrame)
        self.searchFrame = tk.Frame(self)
        self.searchBar = customEntry(self.searchFrame, isPassword=False, placeHolder="Search by name")
        self.searchButton = tk.Button(self.searchFrame)
        self.widgetsConfig()
        return

    def widgetsConfig(self):
        self.titleLabel.configure(text="Select a category", font=("forest-dark", 30, "bold"))
        self.noviceButton.configure(text="Novice", command=lambda: self.filterContender("Novice"))
        self.intermediateButton.configure(text="Intermediate", command=lambda: self.filterContender("Intermediate"))
        self.advancedButton.configure(text="Advanced", command=lambda: self.filterContender("Advanced"))
        self.cancelButton.configure(text="Cancel", command=lambda: self.master.showFrame("Dashboard"))
        self.searchBar.configure(width=40)
        self.searchButton.configure(text="Search", command=self.filterContender)
        self.treeView.configure(
            height=15, 
            columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"), 
            xscrollcommand=self.scrollbar.set
        )
        self.treeView.bind('<<TreeviewSelect>>', self.showPlaces)

        self.treeView.column("#0", width=40)
        self.treeView.heading("#0", text="ID", anchor="w")
        self.treeView.column("#1", width=270)
        self.treeView.heading("#1", text="Name", anchor="w")
        self.treeView.column("#2", width=40)
        self.treeView.heading("#2", text="Age", anchor="w")
        self.treeView.column("#3", width=175)
        self.treeView.heading("#3", text="Curp", anchor="w")
        self.treeView.column("#4", width=80)
        self.treeView.heading("#4", text="Gender", anchor="w")
        self.treeView.heading("#5", text="Address", anchor="w")
        self.treeView.heading("#6", text="School", anchor="w")
        self.treeView.column("#7", width=120)
        self.treeView.heading("#7", text="Category", anchor="w")
        self.treeView.column("#8", width=80)
        self.treeView.heading("#8", text="Payment", anchor="w")

        self.scrollbar.configure(orient='horizontal', command=self.treeView.xview)
        self.render()
        return
    
    def filterContender(self, filter="Novice"):
        query = self.searchBar.get()
        contenders = None
        if query == self.searchBar.placeHolder:
            contenders = self.cursor.filterContenders(filter=filter, query=None)
        else:
            contenders = self.cursor.filterContenders(query=query, filter=filter)
        
        registers = self.treeView.get_children()
        for element in registers:
            self.treeView.delete(element)
        for contender in contenders:
            self.treeView.insert("", "end", text=contender[0], values=(
                contender[1], contender[2], contender[3], contender[4], contender[5], contender[6], contender[7], contender[8]))
        return
    
    def showPlaces(self, e):
        top = tkinter.Toplevel(self)
        selected = self.treeView.focus()
        names = self.treeView.item(selected)["values"][0].split()
        contender = {
            "name": names[0],
            "firstLastName": names[1],
            "secondLastName": names[2],
            "category": self.treeView.item(selected)["values"][6]
        }
        def proceed():
            self.docMaker.createWinnerCertificate(contender=contender, place='1st place')
            top.destroy()

        def cancel():
            self.docMaker.createWinnerCertificate(contender=contender, place='2nd place')
            top.destroy()

        def delete():
            self.docMaker.createWinnerCertificate(contender=contender, place='3rd place')
            top.destroy()

        label = tk.Label(top, text="Select the place of the contender")
        label.pack(pady=10)

        button_proceed = tk.Button(top, text="1st place", command=proceed)
        button_proceed.pack(pady=10)

        button_cancel = tk.Button(top, text="2nd place", command=cancel)
        button_cancel.pack(pady=10)

        button_delete = tk.Button(top, text="3rd place", command=delete)
        button_delete.pack(pady=10)
        return

    def pack(self, **kargs):
        self.onFocus()
        super().pack(**kargs)

    def onFocus(self):
        registers = self.treeView.get_children()
        for element in registers:
            self.treeView.delete(element)

        contenders = self.cursor.getContenders()
        for contender in contenders:
            self.treeView.insert("", "end", text=contender[0], values=(
                contender[1], contender[2], contender[3], contender[4], contender[5], contender[6], contender[7], contender[8]))
        return
    
    def render(self):
        self.titleLabel.pack()
        self.buttonFrame.pack(pady=10)
        self.noviceButton.grid(row=0, column=0, padx=10)
        self.intermediateButton.grid(row=0, column=1, padx=10)
        self.advancedButton.grid(row=0, column=2, padx=10)
        self.cancelButton.grid(row=0, column=3, padx=10)
        self.treeView.pack(side='left', fill='both', expand=True)
        self.scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')
        self.searchFrame.pack(pady=10)
        self.searchBar.grid(column=0, row=0, padx=10)
        self.searchButton.grid(column=1, row=0)
        self.treeFrame.pack()
        return
