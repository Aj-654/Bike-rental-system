from tkinter import *
from tkinter import ttk
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import messagebox
from start import start
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import test6
import rentabike
import viewbikeshome
import bookinghistoryfinal
import customerprofile
import mysql.connector
class customer:
    def __init__(self,root,userid):
        self.viewbikesframe = None
        self.rentingformframe = None
        self.root = root
        self.root.title("Customer Page")
        self.root.geometry("1920x1080")

        global uid
        uid = userid
        
        img1=Image.open(r"D:\SEM4 MINI PROJECT\startbg2.png")
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1)
        lblimg.place(x=0,y=0,relheight=1,relwidth=1)

        custmenu = LabelFrame(self.root,font=("Baskerville Old Face",28,"bold"),bg="black")
        custmenu.place(x=0,y=0,width=300,height=1080)

        welcome = Label(self.root,text="Welcome,Customer",font=("Baskerville Old Face",24,"bold"),bg="black",fg="white")
        welcome.place(x=10,y=10)

        viewbikes = Button(self.root,text="Book a Bike",font=("Microsoft YaHei UI light",24,"bold"),command=self.viewbikes1,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        viewbikes.place(x=10,y=70)

        '''bookbikes = Button(self.root,text="Book a Bike",font=("Microsoft YaHei UI light",24,"bold"),command=self.book_bike,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        bookbikes.place(x=10,y=130)'''

        bookinghistory = Button(self.root,text="Booking History",font=("Microsoft YaHei UI light",24,"bold"),command=self.viewbooking,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        bookinghistory.place(x=10,y=190)

        userrental = Button(self.root,text="Rent a Bike",font=("Microsoft YaHei UI light",24,"bold"),command=self.rentingform,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        userrental.place(x=10,y=250)

        logoutbutton = Button(self.root,text="Logout",font=("Microsoft YaHei UI light",24,"bold"),command=self.confirm_logout,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        logoutbutton.place(x=10,y=700)

        profilebutton = Button(self.root,text="View Profile",font=("Microsoft YaHei UI light",24,"bold"),command=self.userprofile,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        profilebutton.place(x=10,y=600)

    
        #view profile buttons

        

        rentinglbl1 = Label()

        


    def viewbikes1(self):
        self.viewbikesframe=viewbikeshome.viewbikeshome(self.root,uid)

        
        


    def bookingframe2(self):
        selected_option = self.city_combobox.get()

        if not selected_option:
            messagebox.showerror("Error", "Please select an option.")
        else:
            self.rentalmode.place(x=0,y=70,relheight=1,relwidth=1)

    def userprofile(self):
        self.userprofileframe = customerprofile.customerprofile(self.root,uid)
        
        
        



    def open_window(self):
        option = self.categoryoptions.get()
        if option=="Bike":
            print("Option Bike")
        elif option=="Scooter":
            print("Scooter")
        elif option=="Electric Bike":
            print("electric bike")
        elif option =="Bicycle":
            print("bicycle")

    
        
    '''def book_bike(self):
        if not self.viewbikesframe:
            self.viewbikesframe = viewbikeshome.viewbikeshome(self.root)
        elif not self.rentingformframe:
            self.rentingformframe = rentabike.RentaBike(self.root)

    # check if viewbikesframe exists and forget it if it does
        if self.viewbikesframe and self.viewbikesframe.winfo_exists():
            self.viewbikesframe.place_forget()
            
            self.profileframe.place_forget()
            self.bookingframe.place(x=300,y=0,width=1620,height=1080)

        if self.rentingformframe and self.rentingformframe.winfo_exists():
            self.rentingformframe.place_forget()
            self.bookingframe.place(x=300,y=0,width=1620,height=1080)'''

    def hide_frame(self):
        self.bookingframe.place_forget()

    def hourlyoptions(self):
        self.rentalframe.place(x=0,y=260,height=500,width=1620)
        selected_option = self.city_combobox.get()
        option = self.categoryoptions.get()
        avllabel = Label(self.rentalframe,text="Available Bikes:",font=("Microsoft YaHei UI light",20,"bold"),bg = "pink")
        avllabel.place(x=5,y=5)
        if option=="Bike":
            connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
            cursor = connection.cursor()
            query= "select bikename from bikes where category='Bike' and rentalmode='hourly'"
            cursor.execute(query)
            row = cursor.fetchall()
            if row!=None:
                self.listbox = Listbox(self.rentalframe, height = 10,width = 30,bg = "pink",activestyle = 'dotbox',font=("Microsoft YaHei UI light",20,"bold"),bd=0, highlightthickness=0)
                self.listbox.place(x=40,y=60)
                for item in row:
                    self.listbox.insert(END, item)
                    
        elif option=="Scooter":
            print("Scooter")
    
    def rentingform(self):
        
        self.rentingformframe = rentabike.RentaBike(self.root)
        

    def showdetails(self):
        for i in self.listbox.curselection():
            var = (self.listbox.get(i))
            connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
            cursor = connection.cursor()
            query= "select bikename from bikes where category='Bike' and rentalmode='hourly'"
            cursor.execute(query)
            row = cursor.fetchall()

    def submit_form(self):
        # get values from form widgets
        rental_type = self.modeoptions.get()
        start_date = datetime.strptime(self.start_date.get(), "%Y-%m-%d").date()

        if rental_type == "Monthly":
            end_date = (start_date.replace(day=1) + timedelta(days=31)).replace(day=start_date.day)
            self.end_date.set_date(end_date.strftime("%Y-%m-%d"))
            print(start_date)
            print(end_date)
        else:
            end_date = datetime.strptime(self.end_date.get(), "%Y-%m-%d").date()

            # check for valid end date based on rental type
            if rental_type == "Hourly":
                max_end_date = start_date + timedelta(days=3)
                if end_date > max_end_date:
                    messagebox.showerror("Invalid End Date", "End date cannot be more than 3 days after start date.")
                    return

    def monthlyoptions(self):
        self.rentalframe.place(x=0,y=260,height=700,width=1620)

    def viewbooking(self):
        self.viewbookingframe = bookinghistoryfinal.bookinghistory(self.root,uid)

    def confirm_logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root= Tk()
    userid = None
    window = customer(root,userid)
    root.mainloop()    