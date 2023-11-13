import tkinter
from tkinter import *
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from tkinter import messagebox
import bookabikepg2


class bookabike(tkinter.Frame):
    def __init__(self,root,varname,varmileage,varengine,varfront,varrear,vardisplacement,varfuelcapcity,varbodytype,varspeedometer,varodometer,varimagedata,varcategory,uid):
        super().__init__(root)
        self.root = root
        self.config(width=1620,height=1080)
        self.place(x=0,y=0)
        global userid
        userid = uid
        '''hideframe = Button(self,text="View Bikes",font=("Microsoft YaHei UI light",24,"bold"),command=self.hide_frame,bg="black",fg="white",activebackground="black",activeforeground="black",bd=0, highlightthickness=0)
        hideframe.place(x=760,y=450)'''
        self.varname=varname
        self.varmileage=varmileage
        self.varengine=varengine
        self.varfront=varfront
        self.varrear=varrear
        self.vardisplacement=vardisplacement
        self.varfuelcapacity=varfuelcapcity
        self.varbodytype=varbodytype
        self.varspeedometer=varspeedometer
        self.varodometer=varodometer
        self.varimagedata=varimagedata
        self.varcategory=varcategory
        img2=Image.open(r"D:\SEM4 MINI PROJECT\startbg1.png")
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        bookingimg=Label(self,image=self.photoimg2)
        bookingimg.place(x=0,y=0,relheight=1,relwidth=1)

        citylabel2 = Label(self,font=("Microsoft YaHei UI light",24,"bold"))
        citylabel2.place(x=0,y=0,height=70,width=1620)

        citylabel = Label(self,text="Select Your city:",font=("Microsoft YaHei UI light",24,"bold"))
        citylabel.place(x=20,y=20)

        # List of cities in India
        cities = ["Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Jaipur", "Kolkata", "Mumbai", "Pune"]

        # Create a combobox with all the cities
        self.city_combobox = ttk.Combobox(self, values=cities,font=("Microsoft YaHei UI light",24,"bold"))
        self.city_combobox.place(x=300,y=20)

        gobutton = Button(self,text="Go->",font=("Microsoft YaHei UI light",22,"bold"),command=self.bookingframe2,height=1,bd=0, highlightthickness=0)
        gobutton.place(x=760,y=10)

        self.rentalmode = Frame(self)

        img3=Image.open(r"D:\SEM4 MINI PROJECT\sclock2.png")
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        self.categoryoptions = StringVar()
        self.modeoptions = StringVar()
        self.fueloptions = StringVar()

        hourlybutton=Radiobutton(self.rentalmode,image=self.photoimg3,variable=self.modeoptions,value='Hourly',bd=0, highlightthickness=0)
        hourlybutton.place(x=90,y=100,width=100,height=100)

        selectlabel = Label(self.rentalmode,text="Select a Rental Mode!",font=("Microsoft YaHei UI light",22,"bold"))
        selectlabel.place(x=70,y=40)

        hourlylabel = Label(self.rentalmode,text="Hourly Rental",font=("Microsoft YaHei UI light",20,"bold"))
        hourlylabel.place(x=50,y=200)

        orlabel = Label(self.rentalmode,text="OR",font=("Microsoft YaHei UI light",22,"bold"))
        orlabel = Label(self.rentalmode,text="OR",font=("Microsoft YaHei UI light",22,"bold"))
        orlabel.place(x=250,y=130)

        img4=Image.open(r"D:\SEM4 MINI PROJECT\scalendar2.png")
        self.photoimg4=ImageTk.PhotoImage(img4)
        monthlybutton=Radiobutton(self.rentalmode,image=self.photoimg4,variable=self.modeoptions,value='Monthly',bd=0, highlightthickness=0)
        monthlybutton.place(x=360,y=100,width=100,height=100)

        monthlylabel = Label(self.rentalmode,text="Monthly Subscription",font=("Microsoft YaHei UI light",20,"bold"))
        monthlylabel.place(x=290,y=200)

        self.rentalframe = Frame(self.rentalmode,bg="pink")
        

        '''categorylabel = Label(self.rentalmode,text="Choose a Category:",font=("Microsoft YaHei UI light",22,"bold"))
        categorylabel.place(x=50,y=40)

        

        self.rb1 = Radiobutton(self.rentalmode, text="Bike", variable=self.categoryoptions, value="Bike",font=("Microsoft YaHei UI light",20))
        self.rb1.place(x=50,y=100)
        self.rb2 = Radiobutton(self.rentalmode, text="Scooter", variable=self.categoryoptions, value="Scooter",font=("Microsoft YaHei UI light",20),)
        self.rb2.place(x=50,y=150)
        self.rb3 = Radiobutton(self.rentalmode, text="Electric Bike", variable=self.categoryoptions, value="Electric Bike",font=("Microsoft YaHei UI light",20),)
        self.rb3.place(x=50,y=200)
        self.rb4 = Radiobutton(self.rentalmode, text="Bicycle", variable=self.categoryoptions, value="Bicycle",font=("Microsoft YaHei UI light",20),)
        self.rb4.place(x=50,y=250)'''

        '''selectbutton = Button(self.rentalframe,text="Select this bike",font=("Microsoft YaHei UI light",20),bd=0, highlightthickness=0)
        selectbutton.place(x=500,y=400)'''
        self.fueloptionbutton = Label(self.rentalmode,text="Select if you want fuel to be pre-filled",font=("Microsoft YaHei UI light",20,"bold"))
        self.fueloptionbutton.place(x=50,y=450)
        self.withfueloption = Radiobutton(self.rentalmode, text="I want the fuel prefilled", variable=self.fueloptions, value="fuelyes",font=("Microsoft YaHei UI light",20))
        self.withfueloption.place(x=50,y=500)
        self.withoutfueloption = Radiobutton(self.rentalmode, text="I do not want any fuel ", variable=self.fueloptions, value="fuelno",font=("Microsoft YaHei UI light",20))
        self.withoutfueloption.place(x=500,y=500)
        # create submit button
        self.submit_button = Button(self.rentalmode, text="Next",font=("Microsoft YaHei UI light",20,"bold"),command=self.submit_form)
        self.submit_button.place(x=50,y=600)
        

        # create label and calendar widget for start date
        self.startdatelabel = Label(self.rentalmode, text="Start Date:",font=("Microsoft YaHei UI light",20,"bold"))
        self.startdatelabel.place(x=50,y=250)
        self.start_date = DateEntry(self.rentalmode, width=12,font=("Microsoft YaHei UI light",16), background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
        self.start_date.place(x=200,y=250)

        # create label and calendar widget for end date
        self.enddatelabel = Label(self.rentalmode, text="End Date:",font=("Microsoft YaHei UI light",20,"bold"))
        self.enddatelabel.place(x=50,y=350)
        self.end_date = DateEntry(self.rentalmode, width=12,font=("Microsoft YaHei UI light",16), background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
        self.end_date.place(x=200,y=350)
        
        starttimelabel= ttk.Label(self.rentalmode, text="Start Time:",font=("Microsoft YaHei UI light",20,"bold"))
        starttimelabel.place(x=400,y=250)

        # Add a combobox for the start time
        self.start_time = StringVar()
        self.start_time.set("09:00 AM")
        starttimecombo=ttk.Combobox(self.rentalmode, textvariable=self.start_time, values=self._get_time_range(), state="readonly",font=("Microsoft YaHei UI light",16))
        starttimecombo.place(x=550,y=250)
        

        # Add a label for the end time
        endtimelabel= ttk.Label(self.rentalmode, text="End Time:",font=("Microsoft YaHei UI light",20,"bold"))
        endtimelabel.place(x=400,y=350)

        # Add a combobox for the end time
        self.end_time = StringVar()
        self.end_time.set("09:00 AM")
        endtimecombo=ttk.Combobox(self.rentalmode, textvariable=self.end_time, values=self._get_time_range(), state="readonly",font=("Microsoft YaHei UI light",16))
        endtimecombo.place(x=550,y=350)

    def _get_time_range(self):
        # Generate a list of time strings from 9:00 AM to 6:00 PM in 30-minute increments
        times = []
        start_time = datetime.strptime("09:00 AM", "%I:%M %p")
        end_time = datetime.strptime("10:00 PM", "%I:%M %p")
        while start_time <= end_time:
            times.append(start_time.strftime("%I:%M %p"))
            start_time += timedelta(minutes=60)
        return times

        

    def bookingframe2(self):
        selected_option = self.city_combobox.get()

        if not selected_option:
            messagebox.showerror("Error", "Please select an option.")
        else:
            self.rentalmode.place(x=0,y=70,relheight=1,relwidth=1)

    def submit_form(self):
        # get values from form widgets
        rental_type = self.modeoptions.get()
        start_date = datetime.strptime(self.start_date.get(), "%Y-%m-%d").date()
        fuel_type = self.fueloptions.get()
        starttime=self.start_time.get()
        endtime=self.end_time.get()
        print(starttime)
        print(endtime)
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
                
        self.place_forget()
        nextpage = bookabikepg2.bookabikepg2(self.root,self.varname,self.varmileage,self.varengine,self.varfront,self.varrear,self.vardisplacement,self.varfuelcapacity,self.varbodytype,self.varspeedometer,self.varodometer,self.varimagedata,self.varcategory,rental_type,start_date,end_date,starttime,endtime,fuel_type,userid)    
        

if __name__=='__main__':
    root=Tk()
    window = bookabike(root)
    root.mainloop()