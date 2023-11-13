from tkinter import *
from PIL import Image , ImageTk
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

root = Tk()
root.title('View Scooters')
root.geometry("1500x1000")
root.configure(background="lightblue")

heading = Label(root,text ='Choose your Scooter',bg='lightblue',font=('Microsoft YaHei UI Light',26,'bold'))
heading.place(x=600,y=30)

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




activa_image = Image.open("activa.png")
activa_image_resized = activa_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
activa_photo = ImageTk.PhotoImage(activa_image_resized)
# btn1 = Button(root, image=enfield_photo)

btn1 = Button(root,image=activa_photo,command=scoot1)
btn1.pack(expand=True, fill=BOTH)
btn1.place(x=40,y=100)

activa_label = Label(root, text=" Honda Activa 5G", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
activa_label.pack(expand=True, fill=BOTH)
activa_label.place(x=160, y=360)


jupimain_image = Image.open("jupimain.png")
jupimain_image_resized = jupimain_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
jupimain_photo = ImageTk.PhotoImage(jupimain_image_resized)
btn2 = Button(root,image=jupimain_photo,command=scoot2)
btn2.pack(expand=True, fill=BOTH)
btn2.place(x=40,y=420)

jupimain_label = Label(root, text="Jupiter", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
jupimain_label.pack(expand=True, fill=BOTH)
jupimain_label.place(x=160, y=680)


suzuki_image = Image.open("suzuki.png")
suzuki_image_resized = suzuki_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
suzuki_photo = ImageTk.PhotoImage(suzuki_image_resized)
btn3 = Button(root,image=suzuki_photo,command=scoot3)
btn3.pack(expand=True, fill=BOTH)
btn3.place(x=510,y=100)
suzuki_label = Label(root, text="Suzuki Access 125", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
suzuki_label.pack(expand=True, fill=BOTH)
suzuki_label.place(x=640, y=360)

herosco_image = Image.open("herosco.png")
herosco_image_resized = herosco_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
herosco_photo = ImageTk.PhotoImage(herosco_image_resized)
btn4 = Button(root,image=herosco_photo)
btn4.place(x=510,y=420)
herosco_label = Label(root, text="Hero Xoom 110", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
herosco_label.pack(expand=True, fill=BOTH)
herosco_label.place(x=640, y=680)


hondadio_image = Image.open("hondadio.png")
hondadio_image_resized = hondadio_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
hondadio_photo = ImageTk.PhotoImage(hondadio_image_resized)
btn5 = Button(root,image=hondadio_photo)
btn5.place(x=1000,y=100)
hondadio_label = Label(root, text="Honda Dio", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
hondadio_label.pack(expand=True, fill=BOTH)
hondadio_label.place(x=1150, y=360)


heromast_image = Image.open("heromast.png")
heromast_image_resized = heromast_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
heromast_photo = ImageTk.PhotoImage(heromast_image_resized)
btn6 = Button(root,image=heromast_photo)
btn6.place(x=1000,y=420)
heromast_label = Label(root, text="Hero Maestro Edge 110", bg="lightblue", font=('Microsoft YaHei UI Light', 14, 'bold'))
heromast_label.pack(expand=True, fill=BOTH)
heromast_label.place(x=1110, y=680)
mainloop()