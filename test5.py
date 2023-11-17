from tkinter import *
from tkinter import ttk
import mysql.connector

class BikeDetailsApp:
    def __init__(self, root):
        self.root = root
        self.viewframe = Frame(self.root, bg="gray")
        self.viewframe.place(x=300, y=0, width=1620, height=1080)

        # create a treeview widget
        self.tree = ttk.Treeview(self.viewframe, selectmode='browse')
        self.tree.place(x=0, y=0, width=600, height=600)

        # define columns
        self.tree["columns"] = ("Name")

        # format columns
        self.tree.column("Name", width=150, minwidth=50)

        # create headings
        self.tree.heading("Name", text="Name")

        # bind treeview selection
        self.tree.bind("<ButtonRelease-1>", self.get_bike_details)

        # connect to MySQL database
        self.connection = mysql.connector.connect(host="localhost", database="bike_rental_database", user="root", password="root")

        # get cursor
        self.cursor = self.connection.cursor()

        # fetch bike data
        self.fetch_bike_data()

    def fetch_bike_data(self):
        # clear the treeview
        self.tree.delete(*self.tree.get_children())

        # execute MySQL query
        self.cursor.execute("SELECT bikename FROM bikes")

        # fetch all rows
        rows = self.cursor.fetchall()

        # add data to treeview
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def get_bike_details(self, event):
        # get selected row
        selected_row = self.tree.focus()

        # get bike id
        bike_id = self.tree.item(selected_row)['values'][0]
        res = [bike_id]

        # execute MySQL query
        query = "SELECT bikename, category, availability FROM bikes WHERE bikename=%s"
        self.cursor.execute(query, res)

        # fetch row
        row = self.cursor.fetchone()

        # display details
        if row is not None:
            name_label = Label(self.root, text=f"Name: {row[0]}")
            name_label.place(x=350, y=100)
            brand_label = Label(self.root, text=f"Category: {row[1]}")
            brand_label.place(x=350, y=150)
            price_label = Label(self.root, text=f"Availability: {row[2]}")
            price_label.place(x=350, y=200)


if __name__ == "__main__":
    root = Tk()
    app = BikeDetailsApp(root)
    root.mainloop()

'''import tkinter as tk
import mysql.connector

class BikeDetailsWindow(tk.Toplevel):
    def __init__(self, parent, bike_id):
        super().__init__(parent)
        self.title("Bike Details")
        self.geometry("300x200")

        # create labels to display bike details
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()
        self.category_label = tk.Label(self, text="Category:")
        self.category_label.pack()
        self.availability_label = tk.Label(self, text="Availability:")
        self.availability_label.pack()

        # connect to the database and fetch bike details
        connection = mysql.connector.connect(host="localhost", database="bike_rental_database", user="root", password="root")
        cursor = connection.cursor()
        query = f"SELECT bikename, category, availability FROM bikes WHERE id = {bike_id}"
        cursor.execute(query)
        bike_data = cursor.fetchone()
        cursor.close()
        connection.close()

        # display bike details
        self.name_label.config(text="Name: " + bike_data[0])
        self.category_label.config(text="Category: " + bike_data[1])
        self.availability_label.config(text="Availability: " + bike_data[2])

class BikeTable(.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create table to display bike names
        self.table = tk.ttk.Treeview(self, columns=("Name"), show="headings", height=10)
        self.table.heading("Name", text="Name")
        self.table.pack()

        # connect to the database and fetch bike names
        connection = mysql.connector.connect(host="localhost", database="bike_rental_database", user="root", password="root")
        cursor = connection.cursor()
        query = "SELECT id, bikename FROM bikes"
        cursor.execute(query)
        bike_data = cursor.fetchall()
        cursor.close()
        connection.close()

        # populate the table with bike names
        for row in bike_data:
            self.table.insert("", "end", values=(row[1],), tags=(row[0],))

        # add event handler for double-clicking on a row in the table
        self.table.bind("<Double-1>", self.show_details)

    def show_details(self, event):
        # get the ID of the selected row
        item_id = self.table.item(self.table.selection())["tags"][0]

        # open the bike details window
        details_window = BikeDetailsWindow(self.master, item_id)

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create the bike table
        self.bike_table = BikeTable(self)
        self.bike_table.pack()

        # add a button to close the window
        self.close_button = tk.Button(self, text="Close", command=self.quit)
        self.close_button.pack()

# create the main application window
root = tk.Tk()
root.title("Bike Rental")
app = App(root)
app.pack()

# start the event loop
root.mainloop()'''