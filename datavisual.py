import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector

class ChartApp:
    def __init__(self, root):
        # Connect to MySQL database
        self.root=root
        self.root.geometry("800x600")
        connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
        self.mycursor = connection.cursor()

        # Create a cursor object
        

        # Execute the SQL query to get the data
        self.mycursor.execute("SELECT name, AVG(ratings), COUNT(*) FROM review GROUP BY name")

        # Fetch the data
        data = self.mycursor.fetchall()

        # Create lists to store the data
        self.models = []
        self.averages = []
        self.counts = []

        # Loop through the results and append the data to the lists
        for index, row in enumerate(data):
            self.models.append(row[0])
            self.averages.append(row[1])
            self.counts.append(row[2])

        # Compute the total count of all models
        self.total_count = sum(self.counts)

        # Create a figure object and add a bar chart to it
        self.fig1 = plt.Figure(figsize=(8,6))
        self.ax1 = self.fig1.add_subplot(111)

        # Loop through the models and plot a bar for each model
        for i in range(len(self.models)):
            # Compute the width of the bar based on the count of the model
            width = 0.8 * self.counts[i] / self.total_count
            # Plot the bar
            self.ax1.bar(self.models[i], self.averages[i], width=width, align='center')

        # Create a second cursor object
        self.cursor = connection.cursor()

        # Execute a SELECT statement to retrieve the data for the pie chart
        self.cursor.execute("SELECT models, COUNT(*) FROM orders GROUP BY models")

        # Fetch the data
        data = self.cursor.fetchall()

        # Create a list of labels and a list of values
        self.labels = []
        self.values = []

        for row in data:
            self.labels.append(row[0])
            self.values.append(row[1])

        # Create a pie chart using Matplotlib
        self.fig2, self.ax2 = plt.subplots(figsize=(30, 30))
        self.ax2.pie(self.values, labels=self.labels, autopct='%1.1f%%', startangle=90)
        self.ax2.axis('equal')
        self.ax2.set_title('Pie Chart')

        # Create a Tkinter window and add the charts to it
        

        # Create a canvas for the first chart
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.root)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Create a canvas for the second chart
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.root)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        
if __name__=='__main__':
    root = tk.Tk()
    newwindow=ChartApp(root)
    root.mainloop()
    
    