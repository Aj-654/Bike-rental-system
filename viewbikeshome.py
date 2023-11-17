from tkinter import *
import tkinter
from tkinter import ttk
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import test6



class viewbikeshome(tkinter.Frame):
    def __init__(self,root,uid):
        super().__init__(root)
        self.root = root
        self.configure(bg='grey',width=1620,height=1080)
        self.place(x=300,y=0)
        global userid
        userid=uid

        label1 = Label(self,text="We offer the following Categories!",font=("Microsoft YaHei UI light",24,"bold"))
        label1.place(x=350,y=100)

        label2 = Label(self,text="Kindly select a category",font=("Microsoft YaHei UI light",20))
        label2.place(x=455,y=150)
        self.categoryoptions = StringVar()

        bikebutton = Button(self,text="Bikes",font=("Microsoft YaHei UI light",20),command=self.bikedetailspage,borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',width=10)
        bikebutton.place(x=520,y=200)

        scooterbutton = Button(self,text="Scooter",font=("Microsoft YaHei UI light",20),command=self.scooterdetailspage,borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',width=10)
        scooterbutton.place(x=520,y=300)

        electricbutton = Button(self,text="Electric Bikes",font=("Microsoft YaHei UI light",20),command=self.electricdetailspage,borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',width=10)
        electricbutton.place(x=520,y=400)

        bicyclebutton = Button(self,text="Bicycle",font=("Microsoft YaHei UI light",20),command=self.bicycledetailspage,borderwidth=1, relief='solid', highlightthickness=2, highlightbackground='gray',width=10)
        bicyclebutton.place(x=520,y=500)


    def bikedetailspage(self):
        viewbikeshome.place_forget(self)
        self.categoryoptions.set("Bike")
        category = self.categoryoptions.get()
        self.viewbikesframe = test6.viewbikesframe(self.root,category,userid)
        

    def scooterdetailspage(self):
        viewbikeshome.place_forget(self)
        self.categoryoptions.set("Scooter")
        category = self.categoryoptions.get()
        self.viewbikesframe = test6.viewbikesframe(self.root,category,userid)
        

    def electricdetailspage(self):
        viewbikeshome.place_forget(self)
        self.categoryoptions.set("Electric")
        category = self.categoryoptions.get()
        self.viewbikesframe = test6.viewbikesframe(self.root,category,userid)
        

    def bicycledetailspage(self):
        viewbikeshome.place_forget(self)
        self.categoryoptions.set("Bicycle")
        category = self.categoryoptions.get()
        self.viewbikesframe = test6.viewbikesframe(self.root,category,userid)
        


if __name__=="__main__":
    root=Tk()
    obj=viewbikeshome(root)
    root.mainloop()