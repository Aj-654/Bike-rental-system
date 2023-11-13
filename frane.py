import tkinter as tk
import mysql.connector

# Create the main window
win = tk.Tk()
win.geometry('800x600')
win.title("Check Reviews")
label = tk.Label(win, text="Public Opinions", font=("Arial", 10, "bold"), pady=10)
label.pack(side="top", fill="x")

# Create a Frame widget to hold reviews
reviews_frame = tk.Frame(win)
reviews_frame.pack(fill="both", expand=True)

# Fetch data from database and add it to the reviews frame
con = mysql.connector.connect(host='localhost', user='root', password='student', database='review')
cur = con.cursor()
cur.execute("SELECT * FROM publicr")
rows = cur.fetchall()
for row in rows:
    # Create a Frame widget to hold each review
    review_frame = tk.Frame(reviews_frame, bd=1, relief="solid", pady=10)
    review_frame.pack(side="top", fill="x", padx=10, pady=5)

    # Add the name column to the review frame
    name_label = tk.Label(review_frame, text=row[1], font=("Arial", 12, "bold"))
    name_label.pack(side="top")

    # Add the rating column to the review frame as stars
    rating_frame = tk.Frame(review_frame)
    rating_frame.pack(side="top")

    for i in range(int(row[3])):
        star_label = tk.Label(rating_frame, text="★", font=("Arial", 12), fg="gold")
        star_label.pack(side="left")

    # Add the review column to the review frame
    review_label = tk.Label(review_frame, text=row[4], font=("Arial", 10))
    review_label.pack(side="top")

# Start the main event loop
win.mainloop()
