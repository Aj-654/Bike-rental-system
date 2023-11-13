import tkinter
from tkinter import *
import mysql.connector


class customerprofile(tkinter.Frame):
    def __init__(self,root,uid):
        super().__init__(root)
        self.root=root
        email = uid
        self.place(x=300, y=0, width=1620, height=1080)
        email = uid
        profilelabel1 = Label(self,text="User Profile",font=("Microsoft YaHei UI light",28,"bold"))
        profilelabel1.place(x=10,y=10)

        profilelabel2 = Label(self,text="User Name:",font=("Microsoft YaHei UI light",24,"bold"))
        profilelabel2.place(x=10,y=100)

        profilelabel2 = Label(self,text="User Email-id:",font=("Microsoft YaHei UI light",24,"bold"))
        profilelabel2.place(x=10,y=200)

        profilelabel3 = Label(self,text="Phone No.:",font=("Microsoft YaHei UI light",24,"bold"))
        profilelabel3.place(x=10,y=300)

        profilelabel4 = Label(self,text="Aadhar No.:",font=("Microsoft YaHei UI light",24,"bold"))
        profilelabel4.place(x=500,y=300)

        profilelabel5 = Label(self,text="License ID:",font=("Microsoft YaHei UI light",24,"bold"))
        profilelabel5.place(x=10,y=400)
        
        print(email)
        
        connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
        cursor = connection.cursor()
        query= "select * from customers where email=%s"
        value= [email]
        cursor.execute(query,value)
        row = cursor.fetchone()
        fname = row[1]
        mname = row[2]
        sname = row[3]
        emailid = row[4]
        pno=row[6]
        ano=row[7]
        lno=row[8]
        self.namelabel = Label(self,font=("Microsoft YaHei UI light",24,"bold"))
        self.namelabel.config(text=fname+" "+mname+" "+sname)
        self.namelabel.place(x=250,y=100)

        self.emaillabel = Label(self,font=("Microsoft YaHei UI light",24,"bold"))
        self.emaillabel.config(text=emailid)
        self.emaillabel.place(x=250,y=200)

        self.phonelabel = Label(self,font=("Microsoft YaHei UI light",24,"bold"))
        self.phonelabel.config(text=pno)
        self.phonelabel.place(x=200,y=300)

        self.aadharlabel = Label(self,font=("Microsoft YaHei UI light",24,"bold"))
        self.aadharlabel.config(text=ano)
        self.aadharlabel.place(x=680,y=300)

        self.licenselabel = Label(self,font=("Microsoft YaHei UI light",24,"bold"))
        self.licenselabel.config(text=lno)
        self.licenselabel.place(x=200,y=400)