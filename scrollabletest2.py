from tkinter import *

root = Tk()
root.geometry("500x500")

# Create a canvas with a scrollbar
canvas = Canvas(root, width=400, height=400)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add some components to the canvas using the place method
label1 = Label(canvas, text="Label 1")
label1.place(x=10, y=10)
label2 = Label(canvas, text="Label 2")
label2.place(x=10, y=50)
button1 = Button(canvas, text="Button 1")
button1.place(x=10, y=100)
button2 = Button(canvas, text="Button 2")
button2.place(x=10, y=150)
entry1 = Entry(canvas)
entry1.place(x=10, y=200)

# Set the scrollable region of the canvas
canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()