import tkinter as tk
import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

# Function to handle submit button click
class RentaBike(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.root = root

        self.configure( bg='purple',width=1620,height=1080)
        self.place(x=300,y=0)
        

        # Create the Owner Name label and entry
        self.owner_name_label = Label(self, text="Owner Name:", bg='purple', fg='white',font=("Microsoft YaHei UI light",20))
        self.owner_name_label.place(x=10,y=50)
        self.owner_name_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.owner_name_entry.place( x=250,y=50)

        # Create the Bike Name label and entry
        self.bike_name_label = Label(self, text="Bike Name:", bg='purple', fg='white',font=("Microsoft YaHei UI light",20))
        self.bike_name_label.place(x=10,y=100)

        self.bike_name_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.bike_name_entry.place( x=250,y=100)


        # Create the Mileage label and entry
        self.mileage_label = Label(self, text="Mileage:", bg='purple', fg='white',font=("Microsoft YaHei UI light",20))
        self.mileage_label.place(x=10,y=150)
        self.mileage_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.mileage_entry.place( x=250,y=150)

        # Create the Engine label and entry
        self.engine_label = Label(self, text="Engine:", bg='purple', fg='white',font=("Microsoft YaHei UI light",20))
        self.engine_label.place(x=10,y=200)
        self.engine_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.engine_entry.place( x=250,y=200)

        # Create the Front label and entry
        self.front_label = Label(self, text="Front:",bg="purple",fg="white",font=("Microsoft YaHei UI light",20))
        self.front_label.place(x=10,y=250)
        self.front_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.front_entry.place( x=250,y=250)

        # Create the Rear label and entry
        self.rear_label = Label(self, text="Rear:",bg="purple",fg="white",font=("Microsoft YaHei UI light",20))
        self.rear_label.place(x=10,y=300)
        self.rear_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.rear_entry.place( x=250,y=300)

        # Create the Displacement label and entry
        self.displacement_label = Label(self, text="Displacement:",bg="purple",fg="white",font=("Microsoft YaHei UI light",20))
        self.displacement_label.place(x=10,y=350)
        self.displacement_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.displacement_entry.place( x=250,y=350)

        # Create the Fuel Capacity label and entry
        self.fuel_capacity_label = Label(self, text="Fuel Capacity:",bg="purple",fg="white",font=("Microsoft YaHei UI light",20))
        self.fuel_capacity_label.place(x=10,y=400)
        self.fuel_capacity_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.fuel_capacity_entry.place( x=250,y=400)

        # Create the Body Type and entry
        self.body_type_label = Label(self, text="Body Type:",bg="purple",fg="white",font=("Microsoft YaHei UI light",20))
        self.body_type_label.place(x=10,y=450)
        self.body_type_entry = Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.body_type_entry.place( x=250,y=450)

        # Create the Speedometer and entry
        self.speedometer_label = tk.Label(self, text="Speedometer:", bg="purple", fg="white",font=("Microsoft YaHei UI light",20))
        self.speedometer_label.place(x=10, y=500)
        self.speedometer_entry = tk.Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.speedometer_entry.place( x=250, y=500)

        # Create the Odometer and entry
        self.odometer_label = tk.Label(self, text="Odometer:", bg="purple", fg="white",font=("Microsoft YaHei UI light",20))
        self.odometer_label.place(x=10, y=550)
        self.odometer_entry = tk.Entry(self, bg='white',font=("Microsoft YaHei UI light",20))
        self.odometer_entry.place( x=250, y=550)

        # Create the Upload Image label and button
        self.upload_image_label = Label(self, text="Upload Image:", bg="purple", fg="white",font=("Microsoft YaHei UI light",20))
        self.upload_image_label.place(x=10, y=600)

        self.image_path = StringVar()
        self.image_path.set("No file chosen")
        self.image_path_label = Label(self, textvariable=self.image_path,font=("Microsoft YaHei UI light",20))
        self.image_path_label.place( x=250, y=600)
        self.categorylabel = Label(self, text="Category", bg="purple", fg="white",font=("Microsoft YaHei UI light",20))
        self.categorylabel.place(x=10,y=700)
        self.browse_button = Button(self, text="Browse", command=self.browse_image,font=("Microsoft YaHei UI light",20))
        self.browse_button.place(x=550, y=600)
        self.categoryoptions=StringVar()
        self.rb1 = Radiobutton(self, text="Bike", variable=self.categoryoptions, value="Bike",bg="purple", fg="white",font=("Microsoft YaHei UI light",20))
        self.rb1.place(x=250,y=700)
        self.rb2 = Radiobutton(self, text="Scooter", variable=self.categoryoptions, value="Scooter",bg="purple", fg="white",font=("Microsoft YaHei UI light",20),)
        self.rb2.place(x=550,y=700)
        self.rb3 = Radiobutton(self, text="Electric Bike", variable=self.categoryoptions, value="Electric Bike",bg="purple", fg="white",font=("Microsoft YaHei UI light",20),)
        self.rb3.place(x=750,y=700)
        self.rb4 = Radiobutton(self, text="Bicycle", variable=self.categoryoptions, value="Bicycle",bg="purple", fg="white",font=("Microsoft YaHei UI light",20),)
        self.rb4.place(x=950,y=700)

        # Create the Submit button
        self.submit_button = Button(self, text="Submit", command=self.submit_form,font=("Microsoft YaHei UI light",20))
        self.submit_button.place(x=150, y=750)

    '''def submit(self):
            owner_name = self.owner_name_entry.get()
            bike_name = self.bike_name_entry.get()
            mileage = self.mileage_entry.get()
            engine = self.engine_entry.get()
            front = self.front_entry.get()
            rear = self.rear_entry.get()
            displacement = self.displacement_entry.get()
            fuel_capacity = self.fuel_capacity_entry.get()
            body_type = self.body_type_entry.get()
            speedometer = self.speedometer_entry.get()
            odometer = self.odometer_entry.get()
            
            if(bike_name=="" or displacement==""):
                messagebox.showinfo("Insert Status", "All Fields are required")
            else:
                connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
                cursor = connection.cursor()
                query = ("INSERT INTO bikes (bikename,mileage,engine,front,rear,displacement,fuelcapacity,bodytype,speedometer,odometer,bikeimage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                value = (bike_name,mileage,engine,front,rear,displacement,fuel_capacity,body_type,speedometer,odometer,image_data)
                cursor.execute(query,value)
                connection.commit()
                messagebox.showinfo("Success", "Form submitted successfully!")'''

        # Function to handle reset button click
    def reset(self):
            self.owner_name_entry.delete(0, tk.END)
            self.bike_name_entry.delete(0, tk.END)
            self.mileage_entry.delete(0, tk.END)
            self.engine_entry.delete(0, tk.END)
            self.front_entry.delete(0, tk.END)
            self.rear_entry.delete(0, tk.END)
            self.displacement_entry.delete(0, tk.END)
            self.fuel_capacity_entry.delete(0, tk.END)
            self.body_type_entry.delete(0, tk.END)
            self.speedometer_entry.delete(0, tk.END)
            self.odometer_entry.delete(0, tk.END)


    def browse_image(self):
        global image_path
        image_path = filedialog.askopenfilename()
        # display the selected image
        image = Image.open(image_path)
        image = image.resize((100, 100))
        image = ImageTk.PhotoImage(image)
        self.image_path_label.config(image=image)
        self.image_path_label.image = image
        

    def submit_form(self):
        # get values from entry widgets
        owner_name = self.owner_name_entry.get()
        bike_name = self.bike_name_entry.get()
        mileage = self.mileage_entry.get()
        engine = self.engine_entry.get()
        front = self.front_entry.get()
        rear = self.rear_entry.get()
        displacement = self.displacement_entry.get()
        fuel_capacity = self.fuel_capacity_entry.get()
        body_type = self.body_type_entry.get()
        speedometer = self.speedometer_entry.get()
        odometer = self.odometer_entry.get()
        category=self.categoryoptions.get()
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # do something with the form data (e.g. save to database)
        if(bike_name=="" or displacement==""):
                messagebox.showinfo("Insert Status", "All Fields are required")
        else:
                connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
                cursor = connection.cursor()
                query = ("INSERT INTO approval (bikename,mileage,engine,front,rear,displacement,fuelcapacity,bodytype,speedometer,odometer,bikeimage,ownername,category) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                value = (bike_name,mileage,engine,front,rear,displacement,fuel_capacity,body_type,speedometer,odometer,image_data,owner_name,category)
                cursor.execute(query,value)
                connection.commit()
                messagebox.showinfo("Success", "Your Bike has been sent for approval, We will contact you soon!")
       








if __name__=="__main__":
    root=tk.Tk()
    obj=RentaBike(root)
    root.mainloop()
