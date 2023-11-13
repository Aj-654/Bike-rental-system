from tkinter import *
from PIL import Image , ImageTk
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

root = Tk()
root.title('Electric Zone')
root.geometry("1500x1000")
root.configure(background="lightblue")

heading = Label(root,text ='Choose your Electric Vehicle',bg='lightblue',font=('Microsoft YaHei UI Light',26,'bold'))
heading.place(x=500,y=30)

# pic = PhotoImage(file='downloadimg.gif')
# pic1 = PhotoImage(file='enfield_royal.png')
# pic1 = PhotoImage(file="honda.png")
# pic = PhotoImage(file="activa.png")

def scoot1():
     root.destroy()
     import scot1details
def scoot2():
     root.destroy()
     import bike2details

def scoot3():
     root.destroy()
     import bike3details




ebike1_image = Image.open("ebike1.png")
ebike1_image_resized = ebike1_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
ebike1_photo = ImageTk.PhotoImage(ebike1_image_resized)
# btn1 = Button(root, image=enfield_photo)

btn1 = Button(root,image=ebike1_photo,command=scoot1)
btn1.pack(expand=True, fill=BOTH)
btn1.place(x=40,y=100)

ebike1_label = Label(root, text="Revolt RV 400", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
ebike1_label.pack(expand=True, fill=BOTH)
ebike1_label.place(x=160, y=360)

ebike2_image = Image.open("ebike2.png")
ebike2_image_resized = ebike2_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
ebike2_photo = ImageTk.PhotoImage(ebike2_image_resized)
btn2 = Button(root,image=ebike2_photo,command=scoot2)
btn2.pack(expand=True, fill=BOTH)
btn2.place(x=40,y=420)

ebike2_label = Label(root, text="Tork Kratos", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
ebike2_label.pack(expand=True, fill=BOTH)
ebike2_label.place(x=160, y=680)


ebike3_image = Image.open("ebike3.png")
ebike3_image_resized = ebike3_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
ebike3_photo = ImageTk.PhotoImage(ebike3_image_resized)
btn3 = Button(root,image=ebike3_photo,command=scoot3)
btn3.pack(expand=True, fill=BOTH)
btn3.place(x=510,y=100)
ebike3_label = Label(root, text="Hop OXO", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
ebike3_label.pack(expand=True, fill=BOTH)
ebike3_label.place(x=640, y=360)

esco4_image = Image.open("esco4.png")
esco4_image_resized = esco4_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
esco4_photo = ImageTk.PhotoImage(esco4_image_resized)
btn4 = Button(root,image=esco4_photo)
btn4.place(x=510,y=420)
esco4_label = Label(root, text="Bajaj Chetak", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
esco4_label.pack(expand=True, fill=BOTH)
esco4_label.place(x=640, y=680)

esco5_image = Image.open("esco5.png")
esco5_image_resized = esco5_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
esco5_photo = ImageTk.PhotoImage(esco5_image_resized)
btn5 = Button(root,image=esco5_photo)
btn5.place(x=1000,y=100)
esco5_label = Label(root, text="Ola S1", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
esco5_label.pack(expand=True, fill=BOTH)
esco5_label.place(x=1150, y=360)


esco6_image = Image.open("esco6.png")
esco6_image_resized = esco6_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
esco6_photo = ImageTk.PhotoImage(esco6_image_resized)
btn6 = Button(root,image=esco6_photo)
btn6.place(x=1000,y=420)
esco6_label = Label(root, text="Hero Electric Optima", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
esco6_label.pack(expand=True, fill=BOTH)
esco6_label.place(x=1110, y=680)
mainloop()