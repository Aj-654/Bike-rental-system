from tkinter import*
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("BIKE RENTAL SYSTEM")
        self.root.geometry("1295x550+230+220")
        
        #variables
        self.var_firstname=StringVar()
        self.var_middlename=StringVar()
        self.var_lastname=StringVar()
        self.var_phone=StringVar()
        self.var_add=StringVar()
        self.var_aadhar=StringVar()
        self.var_licen=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        
        
        #title
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="purple",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        #Labelframe
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=700,y=50,width=425,height=490)
        
        #labels and entries
        #entry 1
        lbl_first_name=Label(labelframeleft,text="First Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_first_name.grid(row=0,column=0,sticky=W)
        
        entry_firstname=ttk.Entry(labelframeleft,textvariable=self.var_firstname,width=32,font=("arial",13,"bold"))
        entry_firstname.grid(row=0,column=1)
        #middle name
        lbl_middle_name=Label(labelframeleft,text="Middle Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_middle_name.grid(row=1,column=0,sticky=W)
        
        entry_middlename=ttk.Entry(labelframeleft,textvariable=self.var_middlename,width=32,font=("arial",13,"bold"))
        entry_middlename.grid(row=1,column=1)
        #last name
        lbl_last_name=Label(labelframeleft,text="Last Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_last_name.grid(row=2,column=0,sticky=W)
        
        entry_lastname=ttk.Entry(labelframeleft,textvariable=self.var_lastname,width=32,font=("arial",13,"bold"))
        entry_lastname.grid(row=2,column=1)
        #entry 2
        #lbl_cust_num=Label(labelframeleft,text="Phone Number",font=("arial",12,"bold"),padx=2,pady=6)
        #lbl_cust_num.grid(row=1,column=0,sticky=W)
        
        #entry_num=ttk.Entry(labelframeleft,textvariable=self.var_phone,width=32,font=("arial",13,"bold"))
        #entry_num.grid(row=1,column=1)
        #entry 3
        lbl_cust_add=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_add.grid(row=3,column=0,sticky=W)
        
        entry_add=ttk.Entry(labelframeleft,textvariable=self.var_add,width=32,font=("arial",13,"bold"))
        entry_add.grid(row=3,column=1)
        #entry 4
        lbl_cust_aadhar=Label(labelframeleft,text="Aadhar No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_aadhar.grid(row=4,column=0,sticky=W)
        
        entry_aadhar=ttk.Entry(labelframeleft,textvariable=self.var_aadhar,width=32,font=("arial",13,"bold"))
        entry_aadhar.grid(row=4,column=1)
        #entry 5
        lbl_cust_driv=Label(labelframeleft,text="License No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_driv.grid(row=5,column=0,sticky=W)
        
        entry_driv=ttk.Entry(labelframeleft,textvariable=self.var_licen,width=32,font=("arial",13,"bold"))
        entry_driv.grid(row=5,column=1)
        #entry 6
        lbl_cust_email=Label(labelframeleft,text="Email ID",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=6,column=0,sticky=W)
        
        entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=32,font=("arial",13,"bold"))
        entry_email.grid(row=6,column=1)
        #entry 7
        lbl_password=Label(labelframeleft,text="Password",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_password.grid(row=7,column=0,sticky=W)
        
        entry_password=ttk.Entry(labelframeleft,textvariable=self.var_password,width=32,font=("arial",13,"bold"))
        entry_password.grid(row=7,column=1)
        lbl_phoneno=Label(labelframeleft,text="Phone no.:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_phoneno.grid(row=8,column=0,sticky=W)
        
        entry_phoneno=ttk.Entry(labelframeleft,textvariable=self.var_phone,width=32,font=("arial",13,"bold"))
        entry_phoneno.grid(row=8,column=1)
        #button
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=409,height=40)
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="purple",fg="white",width=20)
        btnAdd.grid(row=0,column=0,padx=1)
        #btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="purple",fg="white",width=9)
        #btnUpdate.grid(row=0,column=1,padx=1)
       
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="purple",fg="white",width=20)
        btnReset.grid(row=0,column=3,padx=1)
        
        #search 
        
 
        #Show data table
       
        
        
       
       
        
       
        
        
    def add_data(self):
        if  self.var_licen.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customers(fname,mname,lname,email,password,pno,ano,lno) values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_firstname.get(),self.var_middlename.get(),self.var_lastname.get(),self.var_email.get(),self.var_password.get(),self.var_phone.get(),self.var_aadhar.get(),self.var_licen.get()))
                conn.commit()
                
                conn.close()
                messagebox.showinfo("Sucess","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
            

    '''def update(self):
        if self.var_phone.get()=="":
            messagebox.showerror("Error","Please enter phone number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="rentalbike")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set phoneno.=%s,address=%s,aadharno.=%s,licenseno.=%s,email=%s where name=%s",(self.var_phone.get(),self.var_add.get(),self.var_aadhar.get(),self.var_licen.get(),self.var_email.get(),self.var_name.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)'''
        
             
    
       
    def reset(self):
        self.var_firstname.set("")
        self.var_middlename.set("")
        self.var_lastname.set("")
        self.var_phone.set("")
        self.var_add.set("")
        self.var_aadhar.set("")
        self.var_licen.set("")
        self.var_email.set("")
        self.var_password.set("")
    
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
        
        
        
    
    
    
    
        
    
    
