from tkinter import*
import PIL as pillow
from PIL import Image,ImageTk
from customer import Cust_Win
from newBikeAdd import newBikeAdd
import approval6
import viewbikeshome
import datavisual



class BikeRentSystem:
    def __init__(self,root,emailid):
        self.newframe=None
        self.root=root
        self.root.title("Bike Rental System")
        self.root.geometry("1550x800+0+0")
        self.email=emailid
        
        #first image
        img1=Image.open(r"D:\SEM4 MINI PROJECT\img1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #logo
        '''img2=Image.open(r"")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)'''
        
        #title
        lbl_title=Label(self.root,text="BIKE RENTAL SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        #menu
        lbl_menu=Label(main_frame,text="DASHBOARD",font=("times new roman",20,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
    
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="orange",bd=0,relief=RIDGE,cursor="arrow")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="VIEW BIKE",width=22,font=("times new roman",14,"bold"),command=self.viewbike,bg="black",fg="orange",bd=0,relief=RIDGE,cursor="arrow")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="ADD/DELETE BIKE",command=self.adddeletebike,width=22,font=("times new roman",14,"bold"),bg="black",fg="orange",bd=0,relief=RIDGE,cursor="arrow")
        details_btn.grid(row=2,column=0,pady=1)
        
        cust_btn=Button(btn_frame,text="VIEW STATISTICS",width=22,font=("times new roman",14,"bold"),command=self.viewstats,bg="black",fg="orange",bd=0,relief=RIDGE,cursor="arrow")
        cust_btn.grid(row=3,column=0,pady=1)
        
        cust_btn=Button(btn_frame,text="APPROVAL",width=22,font=("times new roman",14,"bold"),command=self.approvalwindow,bg="black",fg="orange",bd=0,relief=RIDGE,cursor="arrow")
        cust_btn.grid(row=4,column=0,pady=1)
        
        #rightside image
        img3=Image.open(r"D:\SEM4 MINI PROJECT\img4.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=225,y=0,width=1310,height=590)
        
    def approvalwindow(self):
        if not self.newframe:
            self.newframe=viewbikeshome.viewbikeshome(self.root,self.email)
        if self.newframe and self.newframe.winfo_exists():
            self.newframe.place_forget()
        self.newWindow = Toplevel(self.root)
        self.app = approval6.BikeRentalApp(self.newWindow)
    def viewstats(self):
        newWindow = Toplevel(self.root)
        self.app = datavisual.ChartApp(newWindow)
        

        
    def cust_details(self):
        if not self.newframe:
            self.newframe=viewbikeshome.viewbikeshome(self.root,self.email)
        if self.newframe and self.newframe.winfo_exists():
            self.newframe.place_forget()
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
    def adddeletebike(self):
        if not self.newframe:
            self.newframe=viewbikeshome.viewbikeshome(self.root,self.email)
        if self.newframe and self.newframe.winfo_exists():
            self.newframe.place_forget()
        self.new_window=Toplevel(self.root)
        self.app=newBikeAdd(self.new_window)


    def viewbike(self):
        self.newframe=viewbikeshome.viewbikeshome(self.root,self.email)
        
if __name__=="__main__":
    root=Tk()
    emailid=""
    obj=BikeRentSystem(root,emailid)
    root.mainloop()