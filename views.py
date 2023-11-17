from tkinter import *
from PIL import Image , ImageTk
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

root = Tk()
root.title('View Bikes')
root.geometry("1500x1000")
root.configure(background="white")

heading = Label(root,text ='Choose your Bike',bg='white',font=('Microsoft YaHei UI Light',26,'bold'))
heading.place(x=600,y=30)

# pic = PhotoImage(file='downloadimg.gif')
# pic1 = PhotoImage(file='enfield_royal.png')
# pic1 = PhotoImage(file="honda.png")
# pic = PhotoImage(file="activa.png")

def bike1():
     root.destroy()
     import bike1details
def bike2():
     root.destroy()
     import bike2details

def bike3():
     root.destroy()
     import bike3details

def bike4():
     root.destroy()
     import bike4details



enfield_image = Image.open("enfield_royal.png")
enfield_image_resized = enfield_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
enfield_photo = ImageTk.PhotoImage(enfield_image_resized)
# btn1 = Button(root, image=enfield_photo)

btn1 = Button(root,command=bike1)
btn1.pack(expand=True, fill=BOTH)
btn1.place(x=40,y=100)

enfield_label = Label(root, text="Royal Enfield Hunter", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
enfield_label.pack(expand=True, fill=BOTH)
enfield_label.place(x=160, y=360)


honda_image = Image.open("honda.png")
honda_image_resized = honda_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
honda_photo = ImageTk.PhotoImage(honda_image_resized)
btn2 = Button(root,image=honda_photo,command=bike2)
btn2.pack(expand=True, fill=BOTH)
btn2.place(x=40,y=420)

honda_label = Label(root, text="Honda Shine", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
honda_label.pack(expand=True, fill=BOTH)
honda_label.place(x=160, y=680)


hero_image = Image.open("hero.png")
hero_image_resized = hero_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
hero_photo = ImageTk.PhotoImage(hero_image_resized)
btn3 = Button(root,image=hero_photo,command=bike3)
btn3.pack(expand=True, fill=BOTH)
btn3.place(x=510,y=100)
hero_label = Label(root, text="Hero Splendor", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
hero_label.pack(expand=True, fill=BOTH)
hero_label.place(x=640, y=360)

traider_image = Image.open("traider.png")
traider_image_resized = traider_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
traider_photo = ImageTk.PhotoImage(traider_image_resized)
btn4 = Button(root,image=traider_photo,command=bike4)
btn4.pack(expand=True, fill=BOTH)
btn4.place(x=510,y=420)
traider_label = Label(root, text="TVS Traider", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
traider_label.pack(expand=True, fill=BOTH)
traider_label.place(x=640, y=680)


bjpulsar_image = Image.open("bjpulsar.png")
bjpulsar_image_resized = bjpulsar_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
bjpulsar_photo = ImageTk.PhotoImage(bjpulsar_image_resized)
btn5 = Button(root,image=bjpulsar_photo)
btn5.place(x=1000,y=100)
bjpulsar_label = Label(root, text="Bajaj Pulsar", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
bjpulsar_label.pack(expand=True, fill=BOTH)
bjpulsar_label.place(x=1150, y=360)


bjplati_image = Image.open("bjplati.png")
bjplati_image_resized = bjplati_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
bjplati_photo = ImageTk.PhotoImage(bjplati_image_resized)
btn6 = Button(root,image=bjplati_photo)
btn6.place(x=1000,y=420)
bjplati_label = Label(root, text="Bajaj Platina", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
bjplati_label.pack(expand=True, fill=BOTH)
bjplati_label.place(x=1150, y=680)
mainloop()