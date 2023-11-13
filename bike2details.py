from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title('Honda Shine')
root.geometry("1500x1000")
root.configure(border=4,background='white')

def moreD2():
    root.destroy()
    import bike2more
img = (Image.open("honda.png"))

resized_image = img.resize((450,300),Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
bikename = Label(root,bg='white',text="Specifications of Honda Shine",font=('Microsoft YaHei UI Light',27,'bold'))
bikename.place(x=25,y=40)
Label(root,image=new_image,bg='white').place(x=45,y=150)

subhead = Label(root,bg='white',text="Honda Shine",font=('Microsoft YaHei UI Light',23,'bold'))
subhead.place(x=550,y=150)


sp1 = Label(root,bg='white',text='Mileage(overall)    65kmpl',font=('Microsoft YaHei UI Light',15,))
sp1.place(x=45,y=500)
sp2 = Label(root,bg='white',text='Engine Type         Air cooled,BS-VI ENGINE',font=('Microsoft YaHei UI Light',15,))
sp2.place(x=45,y=530)
sp3 = Label(root,bg='white',text='Fuel capacity       10.5L',font=('Microsoft YaHei UI Light',15,))
sp3.place(x=45,y=560)
sp4 = Label(root,bg='white',text='Max Power           10.4PS @ 7500rpm',font=('Microsoft YaHei UI Light',15,))
sp4.place(x=45,y=590)
sp5 = Label(root,bg='white',text='Front Brake          Disc',font=('Microsoft YaHei UI Light',15,))
sp5.place(x=45,y=620)

sp6 = Label(root,bg='white',text='Displacement             124cc',font=('Microsoft YaHei UI Light',15,))
sp6.place(x=550,y=500)
sp7 = Label(root,bg='white',text='Body type                Commuter bikes',font=('Microsoft YaHei UI Light',15,))
sp7.place(x=550,y=530)
sp8 = Label(root,bg='white',text='Speedometer            analog',font=('Microsoft YaHei UI Light',15,))
sp8.place(x=550,y=560)
sp9 = Label(root,bg='white',text='Odometer                 Digital',font=('Microsoft YaHei UI Light',15,))
sp9.place(x=550,y=590)
sp10 = Label(root,bg='white',text='Rear Brake                Disc',font=('Microsoft YaHei UI Light',15,))
sp10.place(x=550,y=620)

# frame1 = Frame(root,width=250,height=250,bg='black')
# frame1.place(x=45,y=670)

subhead2=Label(root,text='Wanna know more about Hunter 350?',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
subhead2.place(x=25,y=700)
btn = Button(root, text="Click me!",width=20,height=2,font=('Microsoft YaHei UI Light',14,'bold'),background='lightblue',command=moreD2)
btn.pack(expand=True, fill=BOTH)
btn.place(x=680, y=700)
mainloop()