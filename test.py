import tkinter as tk
from tkinter import ttk
import mysql.connector

class BikeDetailsFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent, width=320, height=1080)
        self.frame.pack(side="left")

        # create labels to display bike details
        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.pack()
        self.category_label = tk.Label(self.frame, text="Category:")
        self.category_label.pack()
        self.availability_label = tk.Label(self.frame, text="Availability:")
        self.availability_label.pack()

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
    def __init__(self, parent, bike_details_frame):
        self.parent = parent
        self.bike_details_frame = bike_details_frame

        # create table to display bike names
        self.table = tk.ttk.Treeview(self.parent, columns=("Name"), show="headings", height=20)
        self.table.heading("Name", text="Name")
        self.table.pack(side="left", padx=20, pady=20)

        # create vertical scrollbar
        self.scrollbar = tk.Scrollbar(self.parent, orient="vertical", command=self.table.yview)
        self.scrollbar.pack(side="left", fill="y", pady=20)

        # attach scrollbar to table
        self.table.configure(yscrollcommand=self.scrollbar.set)

        # connect to the database and fetch bike names
        connection = mysql.connector.connect(host="localhost", database="bike_rental_database", user="root", password="root")
        cursor = connection.cursor()
        query = "SELECT bikename FROM bikes"
        cursor.execute(query)
        bike_data = cursor.fetchall()
        cursor.close()
        connection.close()

        # populate the table with bike names
        for row in bike_data:
            self.table.insert("", "end", values=(row[0],), tags=(row[0],))

        # add event handler for selecting a row in the table
        self.table.bind("<<TreeviewSelect>>", self.show_details)

    def show_details(self, event):
        # get the ID of the selected row
        item_id = self.table.item(self.table.selection())["values"][0]

        # update the bike details frame
        self.bike_details_frame.update_details(item_id)


class App():
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("1920x1080")
        self.parent.title("Bike Rental")

        # create main frame
        self.main_frame = tk.Frame(self.parent, width=1620, height=1080)
        self.main_frame.place(x=300, y=0)
