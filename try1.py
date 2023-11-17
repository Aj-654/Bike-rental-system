import tkinter
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

win = tkinter.Tk()
win.geometry('700x500')
win.title("Add Your Review")

def validate_input():
    if not all((e1.get(),e3.get(), e5.get('1.0', tkinter.END))):
        messagebox.showerror("Error", "Please fill in all the fields.")
    else:
        Registration()

def on_submit_click():
    messagebox.showinfo("Success", "Your review has been added successfully.")

con = mysql.connector.connect(host='localhost', user='root', password='student')
cur = con.cursor(buffered=True)

try:
    cur.execute("USE review")
except:
    cur.execute("CREATE DATABASE review")
    cur.execute("USE review")

try:
    cur.execute("DESCRIBE publicr")
except:
    cur.execute(
        "CREATE TABLE publicr(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), biken VARCHAR(20), rating INT(1), review VARCHAR(200))")

def Registration():
    cur.execute("INSERT INTO publicr(name, biken, rating, review) VALUES (%s, %s, %s, %s)", (e1.get(), vechile_name.get(), e3.get(), e5.get('1.0', tkinter.END)))
    con.commit()
    on_submit_click()

l1 = tkinter.Label(win, text="Add your reviews")
l2 = tkinter.Label(win, text="Name")
l3 = tkinter.Label(win, text="Vehicle name")
l4 = tkinter.Label(win, text="Rate it out of 5")
l5 = tkinter.Label(win, text="Add your Review")

l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=4, column=1)
l5.grid(row=7, column=1)

e1 = tkinter.Entry(win)
e3 = tkinter.Entry(win)
e5 = tkinter.Text(win, height=7, width=40)

e1.grid(row=2, column=2)
e3.grid(row=4, column=2)
e5.grid(row=7, column=2)

# Create a dropdown list for vehicle name
options = ["Activa ", "Hero Honda ", "Jupiter"]
vechile_name = ttk.Combobox(win, values=options)
vechile_name.current(0)
vechile_name.grid(row=3, column=2)

b = tkinter.Button(win, text='Submit Here', command=validate_input)
b.grid(row=9, column=2)

win.mainloop()
