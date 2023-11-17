from tkinter import *
from tkinter import ttk
import tkinter
import mysql.connector

class BikeDetailsFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(self.parent, width=960, height=1080)
        self.frame.place(x=440, y=0)

        # create labels to display bike details
        self.name_label = Label(self.frame, text="Name:")
        self.name_label.place(x=20, y=0)
        self.category_label = Label(self.frame, text="Category:")
        self.category_label.place(x=20, y=40)
        self.availability_label = Label(self.frame, text="Availability:")
        self.availability_label.place(x=20, y=80)

    def update_details(self, bike_id):
        # connect to the database and fetch bike details
        connection = mysql.connector.connect(host="localhost", database="bike_rental_database", user="root", password="root")
        cursor = connection.cursor()
        query = "SELECT bikename, category, availability FROM bikes WHERE bikename = %s"
        value = [bike_id]
        cursor.execute(query,value)
        bike_data = cursor.fetchone()
        cursor.close()
        connection.close()

        # display bike details
        self.name_label.config(text="Name: " + bike_data[0])
        self.category_label.config(text="Category: " + bike_data[1])
        self.availability_label.config(text="Availability: " + bike_data[2])

class BikeTable():
    def __init__(self, parent):
        self.parent = parent
        
        self.style = ttk.Style()
        self.style.configure('Treeview', rowheight=45)
        # create table to display bike names
        global table
        table = ttk.Treeview(self.parent, columns=("List of available Bikes",), show="headings", height=30)
        table.heading("List of available Bikes", text="List of available Bikes")
        table.tag_configure("my_font", font=("Microsoft YaHei UI light",20))
        self.style1 = ttk.Style()
        self.style1.configure("Treeview.Heading", font=("Microsoft YaHei UI light", 20,"bold"))
        table.tag_configure("my_font", font=("Microsoft YaHei UI light", 20))
        for column in table["columns"]:
            table.heading(column, text=column.title(), command=lambda c=column: self.sort_column(table, c, False), anchor="w")
            table.column(column, width=50, anchor="w")

        table.place(x=0, y=0, width=400)

        # create vertical scrollbar
        self.scrollbar = Scrollbar(self.parent, orient="vertical", command=table.yview)
        self.scrollbar.place(x=400, y=00, height=1080)

        # attach scrollbar to table
        table.configure(yscrollcommand=self.scrollbar.set)

        # connect to the database and fetch bike names