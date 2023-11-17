from tkinter import *
from tkinter import ttk
import tkinter
import mysql.connector
import io
import bookabike
from PIL import ImageTk, Image
import new

class BikeDetailsFrame:
    def __init__(self, parent,gobackcommand):
        self.parent = parent
        self.frame = Frame(self.parent, width=960, height=1080)
        self.frame.place(x=440, y=0)

        

        # create labels to display bike details
        self.name_label = Label(self.frame, font=("Microsoft YaHei UI light", 20))
        self.name_label.place(x=20, y=400)
        self.mileage_label = Label(self.frame, font=("Microsoft YaHei UI light", 20))
        self.mileage_label.place(x=20, y=450)
        self.engine_label = Label(self.frame,font=("Microsoft YaHei UI light", 20))
        self.engine_label.place(x=20,y=500)
        self.front_label = Label(self.frame,font=("Microsoft YaHei UI light", 20))
        self.front_label.place(x=20,y=550)
        self.rear_label = Label(self.frame,font=("Microsoft YaHei UI light", 20))
        self.rear_label.place(x=400,y=550)
        self.displacement_label = Label(self.frame,font=("Microsoft YaHei UI light", 20))
        self.displacement_label.place(x=20,y=600)
        self.fuel_label = Label(self.frame,font=("Microsoft YaHei UI light", 20))
        self.fuel_label.place(x=400,y=600)
        self.bodytype_label = Label(self.frame,font=("Microsoft YaHei UI light", 20))
        self.bodytype_label.place(x=20,y=650)
        self.speedometer_label = Label(self.frame,font=("Microsoft YaHei UI light", 20))
        self.speedometer_label.place(x=20,y=700)
        self.odometer_label = Label(self.frame,font=("Microsoft YaHei UI light", 20))
        self.odometer_label.place(x=20,y=750)
        self.image_label = Label(self.frame)
        self.image_label.place(x=20,y=40)
        

        self.gobackbutton = Button(self.frame,text="Back",font=("Microsoft YaHei UI light", 20),command=gobackcommand)
        self.gobackbutton.place(x=600,y=20)
        

    def update_details(self, bike_id):
        # connect to the database and fetch bike details
        connection = mysql.connector.connect(host="localhost", database="bike_rental_database", user="root", password="root")
        cursor = connection.cursor()
        query = "SELECT bikename,mileage,engine,front,rear,displacement,fuelcapacity,bodytype,speedometer,odometer,bikeimage,category, availability FROM bikes WHERE bikename = %s"
        value = [bike_id]
        cursor.execute(query,value)
        bike_data = cursor.fetchone()
        cursor.close()
        connection.close()

        self.name_label.config(text="")
        self.mileage_label.config(text = "")
        self.engine_label.config(text="")
        self.front_label.config(text="")
        self.rear_label.config(text="")
        self.displacement_label.config(text="")
        self.fuel_label.config(text="")
        self.bodytype_label.config(text="")
        self.speedometer_label.config(text="")
        self.odometer_label.config(text="")
        self.image_label.place_forget()
        
        global varname,varmileage,varengine,varfront,varrear,vardisplacement,varfuelcapcity,varbodytype,varspeedometer,varodometer,varimagedata,varcategory
        varname=bike_data[0]
        varmileage=bike_data[1]
        varengine=bike_data[2]
        varfront=bike_data[3]
        varrear=bike_data[4]
        vardisplacement=bike_data[5]
        varfuelcapcity=bike_data[6]
        varbodytype=bike_data[7]
        varspeedometer=bike_data[8]
        varodometer=bike_data[9]
        varimagedata=bike_data[10]
        varcategory=bike_data[11]
        
        '''self.category_label = Label(self.frame, text="Category:",font=("Microsoft YaHei UI light", 20))
        self.category_label.place(x=20, y=500)'''
        '''self.availability_label = Label(self.frame, text="Engine:",font=("Microsoft YaHei UI light", 20))
        self.availability_label.place(x=20, y=550)'''

        self.name_label.config(text="Name: " + bike_data[0])
        self.mileage_label.config(text = "Mileage: "+ str(bike_data[1])+ " kmpl")
        self.engine_label.config(text="Engine: "+bike_data[2])
        self.front_label.config(text="Front Break: "+bike_data[3])
        self.rear_label.config(text="Rear Break: "+bike_data[4])
        self.displacement_label.config(text="Displacement: "+str(bike_data[5])+" cc")
        self.fuel_label.config(text="Fuel Capacity: "+str(bike_data[6])+" L")
        self.bodytype_label.config(text="Bodytype: "+bike_data[7])
        self.speedometer_label.config(text="Speedometer: "+bike_data[8])
        self.odometer_label.config(text="Odometer: "+bike_data[9])
        image_data = bike_data[10]
        
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((400,300))
        photo_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo_image)
        self.image_label.image = photo_image
        self.image_label.place(x=20,y=40)
        '''self.category_label.config(text="Category: " + bike_data[11])
        self.availability_label.config(text="Availability: " + bike_data[12])'''

    
    

class BikeTable():
    def __init__(self, parent, bike_details_frame,categoryoptions):
        self.parent = parent
        self.bike_details_frame = bike_details_frame
        self.categoryoptions = categoryoptions
        print(self.categoryoptions)
        self.style = ttk.Style()
        self.style.configure('Treeview', rowheight=45)
        # create table to display bike names
        self.table = ttk.Treeview(self.parent, columns=("List of available Bikes",), show="headings", height=30)
        self.table.heading("List of available Bikes", text="List of available Bikes")
        self.table.tag_configure("my_font", font=("Microsoft YaHei UI light",20))
        self.style1 = ttk.Style()
        self.style1.configure("Treeview.Heading", font=("Microsoft YaHei UI light", 20,"bold"))
        self.table.tag_configure("my_font", font=("Microsoft YaHei UI light", 20))
        for column in self.table["columns"]:
            self.table.heading(column, text=column.title(), command=lambda c=column: self.sort_column(self.table, c, False), anchor="w")
            self.table.column(column, width=50, anchor="w")

        self.table.place(x=0, y=0, width=400)

        # create vertical scrollbar
        self.scrollbar = Scrollbar(self.parent, orient="vertical", command=self.table.yview)
        self.scrollbar.place(x=400, y=00, height=1080)

        # attach scrollbar to table
        self.table.configure(yscrollcommand=self.scrollbar.set)

        # connect to the database and fetch bike names
        connection = mysql.connector.connect(host="localhost", database="bike_rental_database", user="root", password="root")
        cursor = connection.cursor()
        query = "SELECT bikename FROM bikes where category=%s"
        value=[self.categoryoptions]
        cursor.execute(query,value)
        bike_data = cursor.fetchall()
        cursor.close()
        connection.close()

        # populate the table with bike names
        for row in bike_data:
            self.table.insert("", "end", values=(row[0],), tags=("my_font",row[0],))

        # add event handler for selecting a row in the table
        self.table.bind("<<TreeviewSelect>>", self.show_details)

        self.bookthisbutton = Button(self.parent,text="Book this bike",font=("Microsoft YaHei UI light", 20),command=self.book_bike)
        self.bookthisbutton.place(x=1000,y=700)

        self.checkreviewsbutton = Button(self.parent,text="Check Reviews",font=("Microsoft YaHei UI light", 20),command=self.showreviews)
        self.checkreviewsbutton.place(x=800,y=700)
        
    def book_bike(self):
        self.table.destroy()
        self.scrollbar.destroy()
    
    # Create new frame for booking
        booking_frame = bookabike.bookabike(self.parent,varname,varmileage,varengine,varfront,varrear,vardisplacement,varfuelcapcity,varbodytype,varspeedometer,varodometer,varimagedata,varcategory,uid)
        
    def showreviews(self):
        self.newWindow = Toplevel(self.parent)
        self.app = new.ReviewsGUI(self.newWindow,varname)


    def show_details(self, event):
        # get the ID of the selected row
        item_id = self.table.item(self.table.selection())["values"][0]

        # update the bike details frame
        self.bike_details_frame.update_details(item_id)


class viewbikesframe(tkinter.Frame):
    def __init__(self, parent,categoryoptions,userid):
        super().__init__(parent)
        self.parent = parent
        self.categoryoptions=categoryoptions
        global uid 
        uid = userid
        self.configure(bg='grey',width=1620,height=1080)
        self.place(x=300,y=0)
        # create the bike details frame
        self.bike_details_frame = BikeDetailsFrame(self,self.hideviewbikes)

        # create the bike table
        self.bike_table = BikeTable(self, self.bike_details_frame,self.categoryoptions)
        


    '''def show_bike_details(self, bike_id):
        # connect to the database and fetch bike details
        connection = mysql.connector.connect(host="localhost", database="bike_rental_database", user="root", password="root")
        cursor = connection.cursor()
        query = "SELECT bikename, category, availability FROM bikes WHERE bikename = %s"
        value = [bike_id]
        cursor.execute(query,value)
        bike_data = cursor.fetchone()
        cursor.close()
        connection.close()

        # display bike details
        self.name_label.config(text="Name: " + bike_data[0])
        self.category_label.config(text="Category: " + bike_data[1])
        self.availability_label.config(text="Availability: " + bike_data[2])'''

    def hideviewbikes(self):
        self.pack_forget()
        

    

