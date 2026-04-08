from tkinter import ttk as tk
from services.data_service import Cursor
from ui.components.button import CustomEntry

class Dashboard (tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.buttonGrid = tk.Frame(self)
        self.mainLabel = tk.Label(self)
        self.addButton = tk.Button(self.buttonGrid)
        self.winnerButton = tk.Button(self.buttonGrid)
        self.logoutButton = tk.Button(self.buttonGrid)
        self.treeFrame = tk.Frame(self)
        self.treeView = tk.Treeview(self.treeFrame)
        self.scrollbar = tk.Scrollbar(self.treeFrame)
        self.searchFrame = tk.Frame(self)
        self.searchBar = CustomEntry(self.searchFrame, isPassword=False, placeHolder="Search by name")
        self.searchButton = tk.Button(self.searchFrame)
        self.cursor = Cursor()

        self.widgetsConfig()

    def widgetsConfig(self):
        self.mainLabel.configure(text="Welcome!", font=("forest-dark", 30, "bold"))

        self.searchBar.configure(width=40)
        self.searchButton.configure(text="Search", command=self.searchContenders)
        self.addButton.configure(text="Add a contender", command=lambda: self.master.showFrame("UserForm"))

        self.winnerButton.configure(text="Choose winners", command=lambda: self.master.showFrame("Winners"))

        self.logoutButton.configure(text="Log out", command=lambda: self.master.showFrame("LogIn"))

        self.treeView.configure(
            height=15, 
            columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"), 
            xscrollcommand=self.scrollbar.set
        )
        self.treeView.bind('<<TreeviewSelect>>', self.selectContender)

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

    def selectContender(self, e):
        selected = self.treeView.focus()
        values = self.treeView.item(selected)["values"]
        text = self.treeView.item(selected)["text"]
        if type(values) is list:
            values.insert(0, text)
            self.master.frames["UserForm"].tempContender = values
            self.master.showFrame("UserForm")
        return
    
    def searchContenders(self):
        query = self.searchBar.get()
        contenders = None
        if query == self.searchBar.placeHolder:
            contenders = self.cursor.getContenders()
        else:
            contenders = self.cursor.searchContender(query=query)
        
        registers = self.treeView.get_children()
        for element in registers:
            self.treeView.delete(element)
        for contender in contenders:
            self.treeView.insert("", "end", text=contender[0], values=(
                contender[1], contender[2], contender[3], contender[4], contender[5], contender[6], contender[7], contender[8]))
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
        self.logoutButton.grid(column=0, row=0, padx=10)
        self.addButton.grid(column=1, row=0, padx=10)
        self.winnerButton.grid(column=2, row=0, padx=10)
        self.mainLabel.pack()
        self.buttonGrid.pack(pady=10)
        self.searchFrame.pack(pady=10)
        self.searchBar.grid(column=0, row=0, padx=10)
        self.searchButton.grid(column=1, row=0)
        self.treeView.pack(side='left', fill='both', expand=True)
        self.scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')
        self.treeFrame.pack()
        return
