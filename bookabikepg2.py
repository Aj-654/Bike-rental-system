import tkinter
from tkinter import *
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from tkinter import messagebox
import io
import mysql.connector
import pymysql

class bookabikepg2(tkinter.Frame):
    def __init__(self,root,varname,varmileage,varengine,varfront,varrear,vardisplacement,varfuelcapcity,varbodytype,varspeedometer,varodometer,varimagedata,varcategory,rental_type,start_date,end_date,starttime,endtime,fuel_type,userid):
        super().__init__(root)
        self.root=root
        self.config(width=1620,height=1080)
        self.place(x=0,y=0)
        global uid 
        uid = userid
        self.category=varcategory
        self.infolabel = Label(self,text="You have selected the following options:",font=("Microsoft YaHei UI light",20))
        self.infolabel.place(x=20,y=30)
        self.name_label = Label(self, font=("Microsoft YaHei UI light", 14))
        self.name_label.place(x=20, y=80)
        self.mileage_label = Label(self, font=("Microsoft YaHei UI light", 14))
        self.mileage_label.place(x=20, y=130)
        self.engine_label = Label(self,font=("Microsoft YaHei UI light", 14))
        self.engine_label.place(x=20,y=180)
        self.front_label = Label(self,font=("Microsoft YaHei UI light", 14))
        self.front_label.place(x=20,y=230)
        self.rear_label = Label(self,font=("Microsoft YaHei UI light", 14))
        self.rear_label.place(x=400,y=230)
        self.displacement_label = Label(self,font=("Microsoft YaHei UI light", 14))
        self.displacement_label.place(x=20,y=280)
        self.fuel_label = Label(self,font=("Microsoft YaHei UI light", 14))
        self.fuel_label.place(x=400,y=280)
        self.bodytype_label = Label(self,font=("Microsoft YaHei UI light", 14))
        self.bodytype_label.place(x=20,y=330)
        self.speedometer_label = Label(self,font=("Microsoft YaHei UI light", 14))
        self.speedometer_label.place(x=20,y=380)
        self.odometer_label = Label(self,font=("Microsoft YaHei UI light", 14))
        self.odometer_label.place(x=400,y=380)
        self.image_label = Label(self)
        self.image_label.place(x=20,y=40)
        self.bikename = varname
        self.name_label.config(text="Name: " + varname)
        self.mileage_label.config(text = "Mileage: "+ str(varmileage)+ " kmpl")
        self.engine_label.config(text="Engine: "+varengine)
        self.front_label.config(text="Front Break: "+varfront)
        self.rear_label.config(text="Rear Break: "+varrear)
        self.displacement_label.config(text="Displacement: "+str(vardisplacement)+" cc")
        self.fuelcapacity = varfuelcapcity
        self.fuel_label.config(text="Fuel Capacity: "+str(varfuelcapcity)+" L")
        self.bodytype_label.config(text="Bodytype: "+varbodytype)
        self.speedometer_label.config(text="Speedometer: "+varspeedometer)
        self.odometer_label.config(text="Odometer: "+varodometer)
        image_data = varimagedata
        
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((400,300))
        photo_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo_image)
        self.image_label.image = photo_image
        self.image_label.place(x=800,y=40)

        self.rentaltype = rental_type
        self.rentaltypelabel = Label(self,font=("Microsoft YaHei UI light",20))
        self.rentaltypelabel.place(x=20,y=430)
        self.rentaltypelabel.config(text="Rental Type: "+rental_type)
        
        self.startdate=start_date
        self.startdatelabel = Label(self,font=("Microsoft YaHei UI light",20))
        self.startdatelabel.place(x=400,y=430)
        self.startdatelabel.config(text="Start date: "+start_date.strftime('%Y-%m-%d'))

        self.enddate=end_date
        self.enddatelabel = Label(self,font=("Microsoft YaHei UI light",20))
        self.enddatelabel.place(x=780,y=430)
        self.enddatelabel.config(text="Start date: "+end_date.strftime('%Y-%m-%d'))
        
        self.start_time=starttime
        self.starttimelabel = Label(self,font=("Microsoft YaHei UI light",20))
        self.starttimelabel.place(x=20,y=480)
        self.starttimelabel.config(text="Start time: "+ self.start_time)

        self.end_time = endtime
        self.endtimelabel = Label(self,font=("Microsoft YaHei UI light",20))
        self.endtimelabel.place(x=400,y=480)
        self.endtimelabel.config(text="End time: "+ self.end_time)

        self.fueloptionlabel = Label(self,font=("Microsoft YaHei UI light",20))
        self.fueloptionlabel.place(x=20,y=530)
        self.fuel_type = fuel_type
        if fuel_type == "fuelyes":
            self.fueloptionlabel.config(text="Fuel: Yes")
        elif fuel_type == "fuelno":
            self.fueloptionlabel.config(text="Fuel: No")


        self.estimationlabel = Label(self,text="With the current Bike and your selected options,the Estimated price will be as follows: ",font=("Microsoft YaHei UI light",20,"bold"))
        self.estimationlabel.place(x=20,y=530)

        self.rate = self.calculateprice()
        self.pricelabel = Label(self,text="₹"+str(self.rate),font=("Microsoft YaHei UI light",20,"bold"))
        self.pricelabel.place(x=20,y=580)

        confirmlabel = Label(self,text="Confirm Booking?",font=("Microsoft YaHei UI light",20))
        confirmlabel.place(x=20,y=630)

        yesbutton = Button(self,text="YES",font=("Microsoft YaHei UI light",20),command =self.placeorder)
        yesbutton.place(x=300,y=630)

        nobutton = Button(self,text="NO",font=("Microsoft YaHei UI light",20))
        nobutton.place(x=400,y=630)

    def placeorder(self):
        bikename=self.bikename
        status = "ongoing"
        price = self.rate
        startdate = self.startdate
        enddate = self.enddate
        category=self.category
        '''start_date = datetime.strptime(startdate, "%Y-%m-%d").date()
        end_date = datetime.strptime(enddate, "%Y-%m-%d").date()'''
        connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
        cursor = connection.cursor()
        query1= "select bikeid from bikes where bikename=%s"
        value1=(bikename,)
        cursor.execute(query1,value1)
        row = cursor.fetchone()
        bikeid = row[0]
        query2 = "select customerid from customers where email=%s"
        value2=(uid,)
        cursor.execute(query2,value2)
        row2 = cursor.fetchone()
        customerid = row2[0]

        query3 = "INSERT into orders(customerid,bikeid,models,status,price,type,startdate) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        value3=(customerid,bikeid,bikename,status,price,category,startdate)
        cursor.execute(query3,value3)
        connection.commit()

        messagebox.showinfo("Success","You have placed the order successfully")
        query4="UPDATE bikes SET qty = qty + 1 WHERE bikeid= %s"
        value4=(bikeid,)
        cursor.execute(query4,value4)
        connection.commit()
        cursor.close()
        connection.close()
        print(bikeid)
        print(bikename)
        print(status)
        print(price)
        print(uid)
        print(customerid)

    def calculateprice(self):
        fuelprice = 106.31
        connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
        cursor = connection.cursor()
        query= "select hourlyrate,monthlyrate from bikes where bikename=%s"
        value=(self.bikename,)
        cursor.execute(query,value)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        hourlyrate=row[0]
        monthlyrate=row[1]

        start_time_obj = datetime.strptime(self.start_time, '%I:%M %p')
        end_time_obj = datetime.strptime(self.end_time, '%I:%M %p')
        # Convert start date and time to datetime object
        start_date_time_obj = datetime.combine(self.startdate, start_time_obj.time())
        # Convert end date and time to datetime object
        end_date_time_obj = datetime.combine(self.enddate, end_time_obj.time())

        diff = end_date_time_obj - start_date_time_obj
        hours = diff.total_seconds() / 3600

        print('Number of hours:', hours)
        print(row)
        cap = self.fuelcapacity
        totalfuelprice = fuelprice * cap
        if self.rentaltype=="Hourly" and self.fuel_type =="fuelyes":
            price = hourlyrate * hours
            finalprice = price+totalfuelprice
        elif self.rentaltype=="Hourly" and self.fuel_type =="fuelno":
            price = hourlyrate * hours
            finalprice = price
        elif self.rentaltype=="Monthly" and self.fuel_type =="fuelyes":
            finalprice = monthlyrate+totalfuelprice
        elif self.rentaltype=="Monthly" and self.fuel_type =="fuelno":
            finalprice = monthlyrate
        return finalprice
    

        





if __name__=='__main__':
    root=Tk()
    window= bookabikepg2(root)
    root.mainloop()