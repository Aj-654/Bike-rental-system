

import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Connect to MySQL database
mydb = mysql.connector.connect(host="localhost", db="minifi", username='root', password='mysql6024', port=3305)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the SQL query to get the data
mycursor.execute("SELECT name, AVG(ratings), COUNT(*) FROM review GROUP BY name")

# Fetch the data
data = mycursor.fetchall()

# Create lists to store the data
models = []
averages = []
counts = []

# Loop through the results and append the data to the lists
for index, row in enumerate(data):
    models.append(row[0])
    averages.append(row[1])
    counts.append(row[2])

# Compute the total count of all models
total_count = sum(counts)

# Create a figure object and add a bar chart to it
fig1 = plt.Figure(figsize=(8,6))
ax1 = fig1.add_subplot(111)

# Loop through the models and plot a bar for each model
for i in range(len(models)):
    # Compute the width of the bar based on the count of the model
    width = 0.8 * counts[i] / total_count
    # Plot the bar
    ax1.bar(models[i], averages[i], width=width, align='center')

# Create a Tkinter window and add the bar chart to it
root = tk.Tk()
root.wm_title("Histogram of Ratings")
root.geometry("800x600")

# Create a canvas for the first chart
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Create a second cursor object
cursor = mydb.cursor()

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
fig2, ax2 = plt.subplots()
fig2, ax2 = plt.subplots(figsize=(30, 30))
ax2.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.set_title('Pie Chart')

# Create a canvas for the second chart
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# Start the Tkinter event loop
tk.mainloop()
