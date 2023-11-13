from tkinter import *
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import io

class newBikeAdd:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1010x500+100+10')
        self.root.title("Add+Bike")
        self.root.resizable()

        

        bikeid = Label(self.root, text='Bike ID:',  font=("Microsoft YaHei UI light",20,"bold"))
        bikeid.place(x=8, y=20)

        bikename = Label(self.root, text='Bike Name:',  font=("Microsoft YaHei UI light",20,"bold"))
        bikename.place(x=10, y=100)
        
        mileage = Label(self.root, text='Mileage:',  font=("Microsoft YaHei UI light",20,"bold"))
        mileage.place(x=10, y=150)

        engine = Label(self.root, text='Engine type:',  font=("Microsoft YaHei UI light",20,"bold"))
        engine.place(x=10, y=200)

        front = Label(self.root, text='Front brake:', font=("Microsoft YaHei UI light",20,"bold"))
        front.place(x=10, y=250)

        rear = Label(self.root, text='Rear brake:', font=("Microsoft YaHei UI light",20,"bold"))
        rear.place(x=10, y=300)

        displacement = Label(self.root, text='Displacement:', font=("Microsoft YaHei UI light",20,"bold"))
        displacement.place(x=610, y=100)

        fuelcapacity = Label(self.root, text='Fuel capacity:', font=("Microsoft YaHei UI light",20,"bold"))
        fuelcapacity.place(x=610, y=150)

        bodytype = Label(self.root, text='Bodytype:', font=("Microsoft YaHei UI light",20,"bold"))
        bodytype.place(x=610, y=200)

        speedometer = Label(self.root, text='Speedometer:',font=("Microsoft YaHei UI light",20,"bold"))
        speedometer.place(x=610, y=250)

        odometer = Label(self.root, text='Odometer:',  font=("Microsoft YaHei UI light",20,"bold"))
        odometer.place(x=610, y=300)

        self.bikeidEntry = Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.bikeidEntry.place(x=190, y=30)

        self.bikenameEntry = Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.bikenameEntry.place(x=200, y=100)
        
        self.mileageEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.mileageEntry.place(x=200, y=150)

        self.engineEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.engineEntry.place(x=200, y=200)

        self.frontEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.frontEntry.place(x=200, y=250)

        self.rearEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.rearEntry.place(x=200, y=300)

        self.displacementEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.displacementEntry.place(x=800, y=100)

        self.fuelcapacityEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.fuelcapacityEntry.place(x=800, y=150)

        self.bodytypeEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.bodytypeEntry.place(x=800, y=200)

        self.speedometerEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.speedometerEntry.place(x=800, y=250)

        self.odometerEntry=Entry(self.root,font=("Microsoft YaHei UI light",20,"bold"))
        self.odometerEntry.place(x=800, y=300)
        Label(self.root, text="Upload Image:",font=("Microsoft YaHei UI light",20)).place(x=10,y=400)
        self.image_path = StringVar()
        self.image_path.set("No file chosen")
        self.image_path_label = Label(self.root, textvariable=self.image_path,font=("Microsoft YaHei UI light",20))
        self.image_path_label.place(x=200,y=400)
        self.browse_button = Button(self.root, text="Browse",font=("Microsoft YaHei UI light",20), command=self.browse_image)
        self.browse_button.place(x=400,y=400)

        insert = Button(self.root, text="SUBMIT", font=("italic", 15), bg="white", command=self.insert)
        insert.place(x=790, y=400)

        self.image_label = Label(self.root)
        

    def browse_image(self):
        # display the selected image
        global image_path
        image_path = filedialog.askopenfilename()
        # display the selected image
        image = Image.open(image_path)
        image = image.resize((100, 100))
        image = ImageTk.PhotoImage(image)
        self.image_path_label.config(image=image)
        self.image_path_label.image = image

        # open image file using Pillow and display it in GUI
        '''image = Image.open(file_path)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=image)'''
        

    def insert(self):
        bikeid = self.bikeidEntry.get()
        bikename = self.bikenameEntry.get()
        mileage= self.mileageEntry.get()
        engine= self.engineEntry.get()
        front= self.frontEntry.get()
        rear= self.rearEntry.get()
        displacement= self.displacementEntry.get()
        fuelcapacity= self.fuelcapacityEntry.get()
        bodytype= self.bodytypeEntry.get()
        speedometer= self.speedometerEntry.get()
        odometer= self.odometerEntry.get()
        with open(image_path, 'rb') as f:
            image_data = f.read()
            

        if(bikename=="" or displacement==""):
            messagebox.showinfo("Insert Status", "All Fields are required")
        else:
            connection = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
            cursor = connection.cursor()
            query = ("INSERT INTO bikes (bikename,mileage,engine,front,rear,displacement,fuelcapacity,bodytype,speedometer,odometer,bikeimage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            value = (bikename,mileage,engine,front,rear,displacement,fuelcapacity,bodytype,speedometer,odometer,image_data)
            cursor.execute(query,value)
            connection.commit()
            messagebox.showinfo("Success", "Form submitted successfully!")

            self.bikeidEntry.delete(0, 'end')
            self.bikenameEntry.delete(0, 'end')
            self.mileageEntry.delete(0, 'end')
            self.engineEntry.delete(0, 'end')
            self.frontEntry.delete(0, 'end')
            self.rearEntry.delete(0, 'end')
            self.displacementEntry.delete(0, 'end') 
            self.fuelcapacityEntry.delete(0, 'end')
            self.bodytypeEntry.delete(0, 'end') 
            self.speedometerEntry.delete(0, 'end')
            self.odometerEntry.delete(0, 'end') 
            self.image_path_label.config(text="No file chosen", font=("Microsoft YaHei UI light", 20))

            messagebox.showinfo("Insert Status", "Inserted Successfully")
            connection.close()

if __name__=="__main__":
    root=Tk()
    obj=newBikeAdd(root)
    root.mainloop()
