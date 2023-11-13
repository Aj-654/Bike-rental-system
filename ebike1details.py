from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title('Revolt RV 400')
root.geometry("1500x1000")
root.configure(border=4,background='white')

def mored():
    root.destroy()
    import ebike1more

img = (Image.open("ebike1.png"))

resized_image = img.resize((450,300),Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
bikename = Label(root,bg='white',text="Specifications of Revolt RV 400",font=('Microsoft YaHei UI Light',27,'bold'))
bikename.place(x=25,y=40)
Label(root,image=new_image,bg='white').place(x=45,y=150)

subhead = Label(root,bg='white',text="Revolt RV 400",font=('Microsoft YaHei UI Light',23,'bold'))
subhead.place(x=550,y=150)
starty = Label(root,background='white',text='⭐⭐⭐  Based on User Review',font=('Microsoft YaHei UI Light',15))
starty.place(x=550,y=200)


sp1 = Label(root,bg='white',text='Mileage(overall)    -',font=('Microsoft YaHei UI Light',15,))
sp1.place(x=45,y=500)
sp2 = Label(root,bg='white',text='Motor Type         Mid Drive',font=('Microsoft YaHei UI Light',15,))
sp2.place(x=45,y=530)
sp3 = Label(root,bg='white',text='Charging time       4.5hours',font=('Microsoft YaHei UI Light',15,))
sp3.place(x=45,y=560)
sp4 = Label(root,bg='white',text='Max Power           20.4PS@6100rpm',font=('Microsoft YaHei UI Light',15,))
sp4.place(x=45,y=590)
sp5 = Label(root,bg='white',text='Front Brake          Disc',font=('Microsoft YaHei UI Light',15,))
sp5.place(x=45,y=620)

sp6 = Label(root,bg='white',text='Displacement             150km/charge',font=('Microsoft YaHei UI Light',15,))
sp6.place(x=550,y=500)
sp7 = Label(root,bg='white',text='Body type                Electric bikes',font=('Microsoft YaHei UI Light',15,))
sp7.place(x=550,y=530)
sp8 = Label(root,bg='white',text='Speed meter            Digital',font=('Microsoft YaHei UI Light',15,))
sp8.place(x=550,y=560)
sp9 = Label(root,bg='white',text='Odometer                 Digital',font=('Microsoft YaHei UI Light',15,))
sp9.place(x=550,y=590)
sp10 = Label(root,bg='white',text='Rear Brake                Disc',font=('Microsoft YaHei UI Light',15,))
sp10.place(x=550,y=620)

subhead2=Label(root,text='Wanna know more about Revolt 400?',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
subhead2.place(x=25,y=700)
btn = Button(root, text="Click me!",width=20,height=2,font=('Microsoft YaHei UI Light',14,'bold'),background='lightblue',command=mored)
btn.pack(expand=True, fill=BOTH)
btn.place(x=680, y=700)
mainloop()