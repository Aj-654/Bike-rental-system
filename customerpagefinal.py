from tkinter import *
from tkinter import ttk
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import messagebox
from start import start
from tkcalendar import DateEntry
from datetime import datetime, timedelta
# import test6
import rentabike
import viewbikeshome
import bookinghistory
import customerprofile
import mysql.connector
import os
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
        bookinghistory.place(x=10,y=130)

        userrental = Button(self.root,text="Rent a Bike",font=("Microsoft YaHei UI light",24,"bold"),command=self.rentingform,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        userrental.place(x=10,y=190)

        # logoutbutton = Button(self.root,text="Logout",font=("Microsoft YaHei UI light",24,"bold"),bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        # logoutbutton.place(x=10,y=
        logoutbutton = Button(self.root, text="Logout", font=("Microsoft YaHei UI light", 24, "bold"), bg="black",
                              fg="white", activebackground="black", activeforeground="black", bd=0,
                              highlightthickness=0, command=self.confirm_logout)
        logoutbutton.place(x=10, y=700)

        profilebutton = Button(self.root,text="View Profile",font=("Microsoft YaHei UI light",24,"bold"),command=self.userprofile,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        profilebutton.place(x=10,y=250)

        

        self.bookingframe = Frame(self.root,bg="gray")

        hideframe = Button(self.bookingframe,text="View Bikes",font=("Microsoft YaHei UI light",24,"bold"),command=self.hide_frame,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        hideframe.place(x=760,y=450)
        
        img2=Image.open(r"D:\SEM4 MINI PROJECT\startbg1.png")
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        bookingimg=Label(self.bookingframe,image=self.photoimg2)
        bookingimg.place(x=0,y=0,relheight=1,relwidth=1)

        citylabel2 = Label(self.bookingframe,font=("Microsoft YaHei UI light",24,"bold"))
        citylabel2.place(x=0,y=0,height=70,width=1620)

        citylabel = Label(self.bookingframe,text="Select Your city:",font=("Microsoft YaHei UI light",24,"bold"))
        citylabel.place(x=20,y=20)

        # List of cities in India
        cities = ["Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Jaipur", "Kolkata", "Mumbai", "Pune"]

        # Create a combobox with all the cities
        self.city_combobox = ttk.Combobox(self.bookingframe, values=cities,font=("Microsoft YaHei UI light",24,"bold"))
        self.city_combobox.place(x=300,y=20)

        gobutton = Button(self.bookingframe,text="Go->",font=("Microsoft YaHei UI light",22,"bold"),command=self.bookingframe2,height=1,bd=0, highlightthickness=0)
        gobutton.place(x=760,y=10)

        self.rentalmode = Frame(self.bookingframe)

        img3=Image.open(r"D:\SEM4 MINI PROJECT\sclock2.png")
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        self.categoryoptions = StringVar()
        self.modeoptions = StringVar()

        hourlybutton=Radiobutton(self.rentalmode,image=self.photoimg3,variable=self.modeoptions,value='Hourly',bd=0, highlightthickness=0)
        hourlybutton.place(x=450,y=100,width=100,height=100)

        selectlabel = Label(self.rentalmode,text="Select a Rental Mode!",font=("Microsoft YaHei UI light",22))
        selectlabel.place(x=500,y=40)

        hourlylabel = Label(self.rentalmode,text="Hourly Rental",font=("Microsoft YaHei UI light",20))
        hourlylabel.place(x=430,y=200)

        orlabel = Label(self.rentalmode,text="OR",font=("Microsoft YaHei UI light",22,"bold"))
        orlabel.place(x=620,y=130)

        img4=Image.open(r"D:\SEM4 MINI PROJECT\scalendar2.png")
        self.photoimg4=ImageTk.PhotoImage(img4)
        monthlybutton=Radiobutton(self.rentalmode,image=self.photoimg4,variable=self.modeoptions,value='Monthly',bd=0, highlightthickness=0)
        monthlybutton.place(x=730,y=100,width=100,height=100)

        monthlylabel = Label(self.rentalmode,text="Monthly Subscription",font=("Microsoft YaHei UI light",20))
        monthlylabel.place(x=670,y=200)

        self.rentalframe = Frame(self.rentalmode,bg="pink")
        self.profileframe = Frame(self.root)

        categorylabel = Label(self.rentalmode,text="Choose a Category:",font=("Microsoft YaHei UI light",22))
        categorylabel.place(x=50,y=40)

        

        self.rb1 = Radiobutton(self.rentalmode, text="Bike", variable=self.categoryoptions, value="Bike", command=self.open_window,font=("Microsoft YaHei UI light",20))
        self.rb1.place(x=50,y=100)
        self.rb2 = Radiobutton(self.rentalmode, text="Scooter", variable=self.categoryoptions, value="Scooter", command=self.open_window,font=("Microsoft YaHei UI light",20),)
        self.rb2.place(x=50,y=150)
        self.rb3 = Radiobutton(self.rentalmode, text="Electric Bike", variable=self.categoryoptions, value="Electric Bike", command=self.open_window,font=("Microsoft YaHei UI light",20),)
        self.rb3.place(x=50,y=200)
        self.rb4 = Radiobutton(self.rentalmode, text="Bicycle", variable=self.categoryoptions, value="Bicycle", command=self.open_window,font=("Microsoft YaHei UI light",20),)
        self.rb4.place(x=50,y=250)

        selectbutton = Button(self.rentalframe,text="Select this bike",font=("Microsoft YaHei UI light",20),command=self.showdetails,bd=0, highlightthickness=0)
        selectbutton.place(x=500,y=400)

        

        # create label and calendar widget for start date
        self.startdatelabel = Label(self.rentalmode, text="Start Date:",font=("Microsoft YaHei UI light",20))
        self.startdatelabel.place(x=50,y=300)
        self.start_date = DateEntry(self.rentalmode, width=12,font=("Microsoft YaHei UI light",16), background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
        self.start_date.place(x=200,y=300)

        # create label and calendar widget for end date
        self.enddatelabel = Label(self.rentalmode, text="End Date:",font=("Microsoft YaHei UI light",20))
        self.enddatelabel.place(x=400,y=300)
        self.end_date = DateEntry(self.rentalmode, width=12,font=("Microsoft YaHei UI light",16), background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
        self.end_date.place(x=550,y=300)

        # create submit button
        self.submit_button = Button(self.rentalmode, text="Submit", command=self.submit_form)
        self.submit_button.place(x=50,y=400)
        

    
        

        #view profile buttons

        

        rentinglbl1 = Label()

    def confirm_logout(self):
        confirm = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")
        if confirm == 'yes':
            self.root.destroy()
            os.system("start.py") # replace with your start.py file name


    def viewbikes1(self):
        self.viewbikesframe=viewbikeshome.viewbikeshome(self.root)

        
        


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
        self.viewbookingframe = bookinghistory.bookinghistory(self.root)




if __name__ == '__main__':
    root= Tk()
    userid = None
    window = customer(root,userid)
    root.mainloop()    