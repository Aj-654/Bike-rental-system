from tkinter import *
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import messagebox
import customer1


import mysql.connector
import landingpage


class start:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Bike Rental System")
        self.root.geometry("1920x1080")

        img1=Image.open(r"D:\SEM4 MINI PROJECT\startbg2.png")
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1)
        lblimg.place(x=0,y=0,relheight=1,relwidth=1)

        titlebg = PhotoImage(file="D:\SEM4 MINI PROJECT\header.png")
        titlelabel = Label(self.root, text="BIKE RENTAL SYSTEM",font=("helvetica",100,"bold italic"),fg="#FF7B27",bg="black")
        titlelabel.pack()

        custlabel = Label(self.root,text ="Customer Login", font=("Baskerville Old Face",28,"bold"),fg="white",bg="black")
        custlabel.place(x=240,y=200)

        namelabel = Label(self.root,text="email-id:", font=("Baskerville Old Face",22,"bold"),fg="white",bg="black")
        namelabel.place(x=80,y=280)

        self.e1 = Entry(self.root,width=28,font=("Baskerville Old Face",22))
        self.e1.place(x=220,y=280)

        passwordlabel = Label(self.root,text="Password:", font=("Baskerville Old Face",22,"bold"),fg="white",bg="black")
        passwordlabel.place(x=80,y=350)

        self.e2 = Entry(self.root,width=28,font=("Baskerville Old Face",22),show="*")
        self.e2.place(x=220,y=350)

        submitbutton = Button(self.root,text="Submit",font=("Baskerville Old Face",22),activebackground = "grey",command=self.userlogin).place(x=300,y=430)

        registerlabel = Label(self.root,text ="Not a Customer? Register first.", font=("Baskerville Old Face",22,"bold"),fg="white",bg="black")
        registerlabel.place(x=180,y=530)

        registerbutton = Button(self.root,text="Register",font=("Baskerville Old Face",22),activebackground = "grey",command=self.custregister).place(x=295,y=580)
        


        adminlabel = Label(self.root,text ="Admin Login", font=("Baskerville Old Face",28,"bold"),fg="white",bg="black")
        adminlabel.place(x=960,y=200)

        namelabel = Label(self.root,text="email-id:", font=("Baskerville Old Face",22,"bold"),fg="white",bg="black")
        namelabel.place(x=780,y=280)

        self.e3 = Entry(self.root,width=28,font=("Baskerville Old Face",22))
        self.e3.place(x=910,y=280)

        passwordlabel = Label(self.root,text="Password:", font=("Baskerville Old Face",22,"bold"),fg="white",bg="black")
        passwordlabel.place(x=780,y=350)

        self.e4 = Entry(self.root,width=28,font=("Baskerville Old Face",22),show="*")
        self.e4.place(x=910,y=350)

        submitbutton2 = Button(self.root,text="Submit",font=("Baskerville Old Face",22),activebackground = "grey",command=self.adminlogin).place(x=1000,y=430)

    def custregister(self):
        newWindow = Toplevel(self.root)
        self.app = customer1.Cust_Win(newWindow)
    def userlogin(self):
        userid = self.e1.get()
        password = self.e2.get()
        print(userid)
        print(password)
        if(userid=="" or password==""):
            messagebox.showinfo("Error","Both details need to be entered")

        else:
            connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
            cursor = connection.cursor()
            query= "select email from customers where email=%s and password=%s"
            value= (userid,password)
            cursor.execute(query,value)
            row = cursor.fetchone()
            if row!=None:
                messagebox.showinfo("Success!","You have successfully logged in.")
                from customerpage import customer
                self.newWindow = Toplevel(self.root)
                self.app = customer(self.newWindow,userid)    

    def adminlogin(self):
        emailid = self.e3.get()
        passwd = self.e4.get()
        if(emailid=="" or passwd==""):
            messagebox.showinfo("Error","Both details need to be entered")

        else:
            connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
            cursor = connection.cursor()
            query= "select emailid from admin where emailid=%s and password=%s"
            value= (emailid,passwd)
            cursor.execute(query,value)
            row = cursor.fetchone()
            if row!=None:
                messagebox.showinfo("Success!","You have successfully logged in.")
                self.newWindow = Toplevel(self.root)
                self.app = landingpage.BikeRentSystem(self.newWindow,emailid)

    def get_val(self):
        print(start.userid)
        print(start.password)




    


           


    


        
        
if __name__=="__main__":
    root=Tk()
    obj=start(root)
    root.mainloop()