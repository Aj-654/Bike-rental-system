import tkinter as tk
import mysql.connector
from tkinter import ttk

# Create the main window
win = tk.Tk()
win.geometry('800x600')
win.title("Check Reviews")
label = tk.Label(win, text="Public Opinions", font=("Arial", 10, "bold"), pady=10)
label.pack(side="top", fill="x")

# Create a Treeview widget
tree = ttk.Treeview(win, columns=("id", "name", "biken", "rating", "review"), show="headings")
tree.column("id", width=50)
tree.column("name", width=100)
tree.column("biken", width=50)
tree.column("rating", width=80)
tree.column("review", width=150)
# tree.column("mobile", width=100)
tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("biken", text="Vehicle Name")
tree.heading("rating", text="Ratings on 5")
tree.heading("review", text="Review")
# tree.heading("mobile", text="Mobile")
# tree.configure(font=("Arial", 10))

# Fetch data from database and add it to the tree
con = mysql.connector.connect(host='localhost', user='root', password='student', database='review')
cur = con.cursor()
cur.execute("SELECT * FROM publicr")
rows = cur.fetchall()
for row in rows:
    tree.insert("", tk.END, values=row)

# Add the tree to the window
tree.pack(fill="both", expand=True)


# Define search function
def search():
    # Clear the tree
    for item in tree.get_children():
        tree.delete(item)

    # Get search term
    search_term = search_entry.get().lower()

    # Fetch data from database that match the search term and add it to the tree
    cur.execute(
        f"SELECT * FROM publicr WHERE LOWER(name) LIKE '%{search_term}%' OR LOWER(biken) LIKE '%{search_term}%' OR LOWER(review) LIKE '%{search_term}%'")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)


# Add search field
search_frame = tk.Frame(win)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Search:")
search_label.pack(side="left")

search_entry = tk.Entry(search_frame)
search_entry.pack(side="left")

search_button = tk.Button(search_frame, text="Search", command=search)
search_button.pack(side="left")

# Start the main event loop
win.mainloop()
