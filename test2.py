import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Load the image
image = tk.PhotoImage(file="startbg.png")

# Add the image to the canvas
canvas.create_image(0, 0, image=image, anchor="nw")

# Add a label on top of the image
label = tk.Label(root, text="Hello, world!", bg=root.cget('bg'))
label.place(x=50, y=50)

root.mainloop()