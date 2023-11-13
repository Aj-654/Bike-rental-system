import tkinter as tk
import mysql.connector

class ReviewsGUI:
    def __init__(self,root,bikename):
        self.win=root
        self.win.geometry('800x600')
        self.win.title("Check Reviews")
        self.bikename=bikename
        # Create the label for the title
        self.label = tk.Label(self.win, text="Public Opinions", font=("Arial", 10, "bold"), pady=10)
        self.label.pack(side="top", fill="x")

        # Create the canvas widget to hold the reviews frame and scrollbar
        self.canvas = tk.Canvas(self.win)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create the frame widget to hold the reviews
        self.reviews_frame = tk.Frame(self.canvas)
        self.reviews_frame.pack(side="top", fill="both", expand=True)

        # Create the scrollbar widget and attach it to the canvas
        self.scrollbar = tk.Scrollbar(self.win, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Add the reviews frame to the canvas and configure it to expand with the canvas
        self.canvas.create_window((0, 0), window=self.reviews_frame, anchor="nw")
        self.reviews_frame.bind("<Configure>", lambda event, canvas=self.canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        # Fetch data from database and add it to the reviews frame
        connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
        cursor = connection.cursor()
        query1 = "SELECT bikeid from bikes where bikename=%s"
        bike=self.bikename
        value1=(bike,)
        cursor.execute(query1,value1)
        row=cursor.fetchone()
        bikeid = row[0]

        query2= "SELECT * from review where name=%s"
        value2=(bike,)
        cursor.execute(query2,value2)

        

        
        self.rows = cursor.fetchall()
        for row in self.rows:
            customerid=row[6]
            connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
            cursor = connection.cursor()
            query3= "SELECT fname from customers where customerid=%s"
            value3=(customerid,)
            cursor.execute(query3,value3)
            row2 = cursor.fetchone()
            custname=row2[0]
            # Create a frame widget to hold each review
            self.review_frame = tk.Frame(self.reviews_frame, bd=1, relief="solid", pady=10, width=780)
            self.review_frame.pack(side="top", fill="x", padx=10, pady=5)

            # Add the name column to the review frame
            self.name_label = tk.Label(self.review_frame, text=custname, font=("Arial", 12, "bold"))
            self.name_label.pack(side="top")

            # Add the rating column to the review frame as stars
            self.rating_frame = tk.Frame(self.review_frame,width=600,height=400)
            self.rating_frame.pack(side="top")

            for i in range(int(row[1])):
                self.star_label = tk.Label(self.rating_frame, text="★", font=("Arial", 12), fg="gold")
                self.star_label.pack(side="left")

            # Add the review column to the review frame
            self.review_label = tk.Label(self.review_frame, text=row[2], font=("Arial", 10))
            self.review_label.pack(side="top")

        # Start the main event loop
        self.win.mainloop()

# Create an instance of the ReviewsGUI class


if __name__=='__main__':
    root = tk.Tk()
    newwindow = ReviewsGUI(root)
    root.mainloop()