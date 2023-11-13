import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from landingpage import BikeRentSystem

root = Tk()
root.geometry ('1010x500+100+10')
root.title("Add+Bike")
root.resizable ()
root.configure(bg='black')


def insert():
    bikeid=bikeidEntry.get()
    bikename=bikenameEntry.get()
    mileage=mileageEntry.get();
    engine=engineEntry.get();
    front=frontEntry.get();
    rear=rearEntry.get();
    displacement=displacementEntry.get();
    fuelcapacity=fuelcapacityEntry.get();
    bodytype=bodytypeEntry.get();
    speedometer=speedometerEntry.get();
    odometer=odometerEntry.get();
     
    if(bikeid=="" or bikename=="" or displacement==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con= mysql.connect (host="localhost",database="bike_rental_database",user="root",password="root")
        cursor = con.cursor()
        cursor.execute("insert into bike values ('"+bikeid+"','"+bikename+"','"+mileage+"','"+engine+"','"+front+"','"+rear+"','"+displacement+"','"+fuelcapacity+"','"+bodytype+"','"+speedometer+"','"+odometer+"')") 
        cursor.execute("commit");

        bikeidEntry.delete(0, 'end')
        bikenameEntry.delete(0, 'end')
        mileageEntry.delete(0, 'end')
        engineEntry.delete(0, 'end')
        frontEntry.delete(0, 'end')
        rearEntry.delete(0, 'end')
        displacementEntry.delete(0, 'end') 
        fuelcapacityEntry.delete(0, 'end')
        bodytypeEntry.delete(0, 'end') 
        speedometerEntry.delete(0, 'end')
        odometerEntry.delete(0, 'end') 
        
        MessageBox.showinfo("Insert Status", "Inserted Successfully"); 
        con.close();

def delete():

    if (bikeidEntry.get() == ""):
        MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost",database="bike_rental_database",user="root",password="root") 
        cursor = con.cursor()
        cursor.execute("delete from bike where bikeid='"+bikeidEntry.get()+"'")
        cursor.execute("commit");
        
        bikeidEntry.delete(0, 'end')
        bikenameEntry.delete(0, 'end')
        mileageEntry.delete(0, 'end')
        engineEntry.delete(0, 'end')
        frontEntry.delete(0, 'end')
        rearEntry.delete(0, 'end')
        displacementEntry.delete(0, 'end') 
        fuelcapacityEntry.delete(0, 'end')
        bodytypeEntry.delete(0, 'end') 
        speedometerEntry.delete(0, 'end')
        odometerEntry.delete(0, 'end') 
        
        MessageBox.showinfo("Delete Status", "Deleted Successfully");
        con.close();
        
def go_back(self):
        self.new_window=Toplevel(self.root)
        self.app=BikeRentSystem(self.new_window)

bikeid = Label(root, text='Bike ID:', fg='#8ec8f5', bg='black', font=("Microsoft YaHei UI light",20,"bold"))
bikeid.place(x=8, y=20)

bikename = Label(root, text='Bike Name:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
bikename.place(x=10, y=100)

mileage = Label(root, text='Mileage:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
mileage.place(x=10, y=150)

engine = Label(root, text='Engine type:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
engine.place(x=10, y=200)

front = Label(root, text='Front brake:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
front.place(x=10, y=250)

rear = Label(root, text='Rear brake:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
rear.place(x=10, y=300)

displacement = Label(root, text='Displacement:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
displacement.place(x=610, y=100)

fuelcapacity = Label(root, text='Fuel capacity:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
fuelcapacity.place(x=610, y=150)

bodytype = Label(root, text='Bodytype:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
bodytype.place(x=610, y=200)

speedometer = Label(root, text='Speedometer:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
speedometer.place(x=610, y=250)

odometer = Label(root, text='Odometer:', fg='#bb70e0', bg='black', font=('Comic Sans MS', 15, 'bold'))
odometer.place(x=610, y=300)

bikeidEntry=Entry ()
bikeidEntry.place(x=190, y=30)

bikenameEntry=Entry ()
bikenameEntry.place(x=200, y=100)

mileageEntry=Entry ()
mileageEntry.place(x=200, y=150)

engineEntry=Entry ()
engineEntry.place(x=200, y=200)

frontEntry=Entry ()
frontEntry.place(x=200, y=250)

rearEntry=Entry ()
rearEntry.place(x=200, y=300)

displacementEntry=Entry ()
displacementEntry.place(x=800, y=100)

fuelcapacityEntry=Entry ()
fuelcapacityEntry.place(x=800, y=150)

bodytypeEntry=Entry ()
bodytypeEntry.place(x=800, y=200)

speedometerEntry=Entry ()
speedometerEntry.place(x=800, y=250)

odometerEntry=Entry ()
odometerEntry.place(x=800, y=300)

backbutton = Button(root,text='BACK',font=("italic", 15), bg="white",command=go_back)
backbutton.place(x=390,y=400)

insert = Button (root, text="SUBMIT", font=("italic", 15), bg="white", command=insert) 
insert.place (x=790, y=400)

delete = Button (root, text="DELETE", font=("italic", 15), bg="white", command=delete) 
delete.place (x=590, y=400)


root.mainloop()