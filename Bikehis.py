# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:11:45 2023

@author: HI
"""

import tkinter
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root=Tk()
root.title("Bike History") 
root.geometry("800x700+400+50")
root.resizable (False, False)

Image_icon=PhotoImage(file="history.png") 
root.iconphoto (False, Image_icon)

TopImage=PhotoImage (file="top.png") 
Label(root, image=TopImage).pack()

dockImage=PhotoImage (file="history.png") 
Label(root, image=dockImage, bg="#32405b"). place (x=30,y=10)

heading=Label(root, text="Your Order History", font="Courier 20 bold", fg="white",bg="#32405b") 
heading.place( x = 250 , y = 20)


global boxImage
boxImage = PhotoImage(file="box1.png")



def place_elements():
    cursor = con.cursor()
    cursor.execute("SELECT bikeid,models FROM orders WHERE customerid = 1 ORDER BY orderid")
    data = cursor.fetchall()
    
    step = 150
    y_increment = 0
    for index, row in enumerate(data):
            bikeid = row[0]
            models = row[1]
            text = Label(root, text=f"{models}" , font=("Impact", 20))
            text.place(x=20, y=80+y_increment)
        
            text = Label(root, text="Start date ", font=("Rockwell", 10))
            text.place(x=20, y=110+y_increment)
        
            label = Label(image=boxImage)
            label.image = boxImage  # This line is important to prevent the image from being garbage collected
            label.place(x=20, y=130+y_increment)
            
            label1 = Label(root, text="    OWNER    ", font=("Helvetica", 15, 'bold'), fg="white", bg="#546c9c")
            label1.place(x=25, y=140+y_increment)
        
            label2 = Label(root, text="    PRICE    ", font=("Helvetica", 15, 'bold'), fg="white", bg="#546c9c")
            label2.place(x=175, y=140+y_increment)
        
            label3 = Label(root, text=" DESCRIPTION ", font=("Helvetica", 15, 'bold'), fg="white", bg="#546c9c")
            label3.place(x=325, y=140+y_increment)
        
            label4 = Label(root, text="    TYPE    ", font=("Helvetica", 15, 'bold'), fg="white", bg="#546c9c")
            label4.place(x=475, y=140+y_increment)
        
            return_button = Button(root, text="RETURN", font=("Helvetica", 12, 'bold'), fg="white", bg="#32405b")
            return_button.place(x=650, y=137+y_increment)
            add_review_button = Button(root, text="REVIEW", font=("Helvetica", 12, 'bold'), fg="white", bg="#32405b")
            add_review_button.place(x=652, y=173+y_increment)
            
            owner = Label(root, text=f"{bikeid}", font=("Helvetica", 15, 'bold'), fg="black", bg="#546c9c")
            owner.place(x=70, y=170+y_increment)
            
            y_increment += step


            
def open_return_window(model):
    return_window = Toplevel(root)
    return_window.geometry("300x200")
    return_window.title("Return")

    message = Label(return_window, text=f"Do you want to return {model}", font=("Helvetica", 14))
    message.place(x=20,y=20)
    
    returnn = Button(return_window, text="RETURN", font=("Helvetica", 12, 'bold'), fg="black", bg="#32405b")
    returnn.place(x=20,y=40)
    


class RatingWidget(Frame):
    def __init__(self, parent, num_stars=5, size=25, active_color="orange", inactive_color="gray"):
        Frame.__init__(self, parent)
        self.num_stars = num_stars
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.size = size
        self.active_stars = 0
        self.stars = []
        self.draw_widget()
        
    def draw_widget(self):
        for i in range(self.num_stars):
            star = Label(self, text="★", font=("Arial", self.size), fg=self.inactive_color)
            star.pack(side=LEFT)
            star.bind("<Button-1>", lambda e, i=i: self.set_active_stars(i+1))
            self.stars.append(star)
    
    def set_active_stars(self, num):
        self.active_stars = num
        for i, star in enumerate(self.stars):
            if i < num:
                star.config(fg=self.active_color)
            else:
                star.config(fg=self.inactive_color)
        con = mysql.connect(host="localhost", db="minifi", username='root', password='mysql6024', port=3305)
        cursor = con.cursor()
        cursor.execute("UPDATE orders SET stars = ? WHERE models= = ?", (self.active_stars, models))
        con.commit()




def open_review_window(model):
    win=Tk()
    win.title("Bike Review") 
    win.geometry("500x300+400+50")
    win.resizable (False, False)
    
    momo=Label(win, text=f"Would you like to rate {model} ?", font=("Helvetica", 14))
    momo.place(x=20,y=20)
    
    rating_widget = RatingWidget(win)
    rating_widget.place(x=20, y=45)
    
    revv=Label(win, text=f"Would you like to write a review of {model} ?", font=("Helvetica", 14))
    revv.place(x=20,y=90)
    con = mysql.connect(host="localhost", db="minifi", username='root', password='mysql6024', port=3305)
    cursor = con.cursor()
    submit = Button(win, text="SUBMIT", font=("Helvetica", 12, 'bold'), fg="black", bg="#32405b", )
    submit.place(x=20,y=200)
    


    
place_elements()


root.mainloop()