# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:44:59 2023

@author: HI
"""

import tkinter as tk
from tkinter import ttk
import mysql.connector


# Connect to the database
conn = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
c = conn.cursor()

# Query the database for column data
c.execute('SELECT customerid FROM orders')
column_data = c.fetchall()

# Create the Tkinter window
root = tk.Tk()
root.geometry('200x100')

# Create a StringVar to hold the selected value of the dropdown menu
selected_value = tk.StringVar()

# Create the dropdown menu
dropdown = ttk.Combobox(root, values=column_data, textvariable=selected_value)
dropdown.pack()

# Run the Tkinter event loop
root.mainloop()

# Close the database connection
conn.close()
