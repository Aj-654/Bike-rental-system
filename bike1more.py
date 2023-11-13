from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title('Know More About Royal Enfield')
root.geometry("1500x1000")
root.configure(border=4,background='white')

# def back1():
#     root.destroy()
#     import bike1details

def back1():
    root.destroy()
    import bike1details
    bike1details.bike1details().show()

btn2 = Button(root, text="Go Back",width=10,height=1,font=('Microsoft YaHei UI Light',14,'bold'),background='lightblue',command=back1)
btn2.pack(expand=True, fill=BOTH)
btn2.place(x=1300, y=17)

heading = Label(root,text='Royal Enfield Hunter User Reviews',bg='white',font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=20,y=15)
subheading = Label(root,text='⭐ 4.2 based on User Reviews',bg='white',font=('Microsoft YaHei UI Light',19))
subheading.place(x=20,y=80)

frame=Frame(root,width=500,height=350,bg='grey',bd=3,borderwidth=1)
frame.place(x=20,y=150)
text_widget = Text(frame, width=35, height=10,font=('Microsoft YaHei UI Light',15,'bold'))
text_widget.pack()
# text_widget.insert(END, "This is\na multiline\ntext.")
text_widget.insert(END, "\n ⭐⭐⭐\n The most affordable scooter\n\n The TVS Jupiter is a fantastic scooter in \n both comfort and efficiency. The ride \n experience is smooth and comfortable. \n\n By Neeraj \n Posted on Mar 25,2023  ")

frame1=Frame(root,width=500,height=350,bg='grey',bd=3,borderwidth=1)
frame1.place(x=490,y=150)
text_widget = Text(frame1, width=38, height=10,font=('Microsoft YaHei UI Light',15,'bold'))
text_widget.pack()
text_widget.insert(END, "\n ⭐⭐\n Overall Good Bike\n\n I am very happy with the bike's performance \n and its fuel capacity. \n\n\n By Swastik \n Posted on Mar 15,2023  ")

frame2=Frame(root,width=500,height=350,bg='grey',bd=3,borderwidth=1)
frame2.place(x=1000,y=150)
text_widget = Text(frame2, width=38, height=10,font=('Microsoft YaHei UI Light',15,'bold'))
text_widget.pack()
text_widget.insert(END, "\n ⭐⭐⭐⭐⭐\n Comfortable riding experience\n\n Hunter 350 is a great bike for small riders. It  provides a comfortable riding experience, the  engine is smooth. \n\n By Ajinkya \n Posted on Mar 15,2023  ")

frame3 = Frame(root, width=1000, height=350, bg='white', bd=3, borderwidth=0)
frame3.place(x=20, y=520)

subhead1=Label(root,text='Closer View of Royal Enfield',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
subhead1.place(x=20,y=470)
image1 = Image.open("royal1.png")
image2 = Image.open("royal2.png")
image3 = Image.open('royal3.png')
image4 = Image.open('royal4.png')
# Resize the images
image1 = image1.resize((300, 200))
image2 = image2.resize((400, 200))
image3 = image3.resize((300,200))
image4 = image4.resize((350,200))

# Convert images to Tkinter format
tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)
tk_image3 = ImageTk.PhotoImage(image3)
tk_image4 = ImageTk.PhotoImage(image4)
# Create labels to display the images in the frame
label1 = Label(frame3, image=tk_image1)
label1.pack(side=LEFT, padx=10, pady=10)
label2 = Label(frame3, image=tk_image2)
label2.pack(side=LEFT, padx=10, pady=10)
label3 = Label(frame3, image=tk_image3)
label3.pack(side=LEFT, padx=10, pady=10)
label3 = Label(frame3, image=tk_image4)
label3.pack(side=LEFT, padx=10, pady=10)

mainloop()