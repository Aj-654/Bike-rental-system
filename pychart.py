# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:27:31 2023

@author: HI
"""

import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Connect to the database
db = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")

# Create a cursor
cursor = db.cursor()

# Execute a SELECT statement to retrieve the data for the pie chart
cursor.execute("SELECT models, COUNT(*) FROM orders GROUP BY models")

# Fetch the data
data = cursor.fetchall()

# Create a list of labels and a list of values
labels = []
values = []

for row in data:
    labels.append(row[0])
    values.append(row[1])

# Create a pie chart using Matplotlib
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Pie Chart')

# Embed the pie chart in a tkinter window using the FigureCanvasTkAgg class
root = tk.Tk()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Display the tkinter window
root.mainloop()