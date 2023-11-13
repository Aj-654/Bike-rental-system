from tkinter import *

root = Tk()
root.title('What we offer')
root.geometry('500x500')
root.configure(background='white')

def Bikes():
    root.destroy()
    import views

def Scooter():
    root.destroy()
    import scootview

def Ebike():
    root.destroy()
    import ebikeview

def custgoback1():
    root.destroy()
    import customerpage

def admingoback1():
    root.destroy()
    import landingpage

subhead = Label(root,text='Welcome',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
subhead.place(x=170,y=10)

tagline = Label(root,text='We offer you the following categories!',bg='white',font=('Microsoft YaHei UI Light',17))
tagline.place(x=65,y=100)

bt1 = Button(root, text="Bikes", bg='white', fg='black', font=('Microsoft YaHei UI Light', 12),
              borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',
              width=10, height=1, padx=10, pady=5,
              activebackground='white', activeforeground='gray',command=Bikes)
bt1.pack(expand=True, fill=BOTH)
bt1.place(x=200, y=150)

bt2 = Button(root, text="Scooters", bg='white', fg='black', font=('Microsoft YaHei UI Light', 12),
              borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',
              width=10, height=1, padx=10, pady=5,
              activebackground='white', activeforeground='gray',command=Scooter)
bt2.pack(expand=True, fill=BOTH)
bt2.place(x=200, y=200)

bt3 = Button(root, text="Electric Zone", bg='white', fg='black', font=('Microsoft YaHei UI Light', 12),
              borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',
              width=10, height=1, padx=10, pady=5,
              activebackground='white', activeforeground='gray',command=Ebike)
bt3.pack(expand=True, fill=BOTH)
bt3.place(x=200, y=250)

custgoback = Button(root,text="Go back to customer page",font=('Microsoft YaHei UI Light', 12),
              borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',
              width=10, height=1, padx=50, pady=5,
              activebackground='white', activeforeground='gray',command=custgoback1)
custgoback.place(x=170, y=300)

admingoback = Button(root,text="Go back to Admin page",font=('Microsoft YaHei UI Light', 12),
              borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',
              width=10, height=1, padx=50, pady=5,
              activebackground='white', activeforeground='gray',command=admingoback1)
admingoback.place(x=170, y=350)


# bt4 = Button(root, text="Bicycle", bg='white', fg='black', font=('Microsoft YaHei UI Light', 12),
#               borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',
#               width=10, height=1, padx=10, pady=5,
#               activebackground='white', activeforeground='gray')
# bt4.place(x=200, y=300)



mainloop()
