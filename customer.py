from tkinter import*
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import smtplib
import os
from email.message import EmailMessage
import ssl
import smtplib



class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("BIKE RENTAL SYSTEM")
        self.root.geometry("1295x550+230+220")
        
        #variables
        self.var_name=StringVar()
        self.var_phone=StringVar()
        self.var_add=StringVar()
        self.var_aadhar=StringVar()
        self.var_licen=StringVar()
        self.var_email=StringVar()
        
        
        #title
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="purple",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        #Labelframe
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"),bg='white')
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        #labels and entries
        #entry 1
        lbl_cust_name=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=0,column=0,sticky=W)
        
        entry_name=Entry(labelframeleft,textvariable=self.var_name,width=32,font=("arial",13,"bold"),highlightthickness=0)
        entry_name.grid(row=0,column=1)
        #entry 2
        lbl_cust_num=Label(labelframeleft,text="Phone Number",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_num.grid(row=1,column=0,sticky=W)
        
        entry_num=ttk.Entry(labelframeleft,textvariable=self.var_phone,width=32,font=("arial",13,"bold"))
        entry_num.grid(row=1,column=1)
        #entry 3
        lbl_cust_add=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_add.grid(row=2,column=0,sticky=W)
        
        entry_add=ttk.Entry(labelframeleft,textvariable=self.var_add,width=32,font=("arial",13,"bold"))
        entry_add.grid(row=2,column=1)
        #entry 4
        lbl_cust_aadhar=Label(labelframeleft,text="Aadhar No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_aadhar.grid(row=3,column=0,sticky=W)
        
        entry_aadhar=ttk.Entry(labelframeleft,textvariable=self.var_aadhar,width=32,font=("arial",13,"bold"))
        entry_aadhar.grid(row=3,column=1)
        #entry 5
        lbl_cust_driv=Label(labelframeleft,text="License No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_driv.grid(row=4,column=0,sticky=W)
        
        entry_driv=ttk.Entry(labelframeleft,textvariable=self.var_licen,width=32,font=("arial",13,"bold"))
        entry_driv.grid(row=4,column=1)
        #entry 6
        lbl_cust_email=Label(labelframeleft,text="Email ID",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=5,column=0,sticky=W)
        
        entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=32,font=("arial",13,"bold"))
        entry_email.grid(row=5,column=1)
        #button
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=409,height=40)
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="purple",fg="white",width=13)
        btnAdd.grid(row=0,column=0,padx=1)
        #btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="purple",fg="white",width=9)
        #btnUpdate.grid(row=0,column=1,padx=1)
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="purple",fg="white",width=13)
        btnDelete.grid(row=0,column=2,padx=1)
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="purple",fg="white",width=13)
        btnReset.grid(row=0,column=3,padx=1)
        
        #search 
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=490)
        
        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="purple",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Phone Number","License No.")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        entry_search=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        entry_search.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="purple",fg="white",width=9)
        btnSearch.grid(row=0,column=3,padx=1)
        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="purple",fg="white",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        #Show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,column=("name","phoneno.","address","aadharno.","licenseno.","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("name",text="Customer Name")
        self.Cust_Details_Table.heading("phoneno.",text="Phone Number")
        self.Cust_Details_Table.heading("address",text="Address")
        self.Cust_Details_Table.heading("aadharno.",text="Aadhar No.")
        self.Cust_Details_Table.heading("licenseno.",text="License No.")
        self.Cust_Details_Table.heading("email",text="Email ID")
        self.Cust_Details_Table["show"]="headings"
        
       
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("phoneno.",width=100)
        self.Cust_Details_Table.column("address",width=100)
        self.Cust_Details_Table.column("aadharno.",width=100)
        self.Cust_Details_Table.column("licenseno.",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


        
    def add_data(self):
        if self.var_name.get()=="" or self.var_licen.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="bike_rental_database")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s)",(self.var_name.get(),self.var_phone.get(),self.var_add.get(),self.var_aadhar.get(),self.var_licen.get(),self.var_email.get()))
                
                email_sender = 'vesitbikerentalsystem@gmail.com'
                email_password= 'tfzcclyabdovxfeo'
                email_receiver = self.var_email.get()

                subject = "Registration Successful"
                body = """
                You have Successfully registered to Bike Rental System.
                Thank you for registering.
                """

                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['Subject'] = subject
                em.set_content(body)

                context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                    smtp.login(email_sender,email_password)
                    smtp.sendmail(email_sender,email_receiver,em.as_string())
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="bike_rental_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()    
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        self.var_name.set(row[0])
        self.var_phone.set(row[1])
        self.var_add.set(row[2])
        self.var_aadhar.set(row[3])
        self.var_licen.set(row[4])
        self.var_email.set(row[5])
    '''def update(self):
        if self.var_phone.get()=="":
            messagebox.showerror("Error","Please enter phone number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="bike_rental_database")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set phoneno.=%s,address=%s,aadharno.=%s,licenseno.=%s,email=%s where name=%s",(self.var_phone.get(),self.var_add.get(),self.var_aadhar.get(),self.var_licen.get(),self.var_email.get(),self.var_name.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)'''
        
             
    def mDelete(self):
        mDelete=messagebox.askyesno("Bike Rental System","Do you want to delete this cutomer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="bike_rental_database")
            my_cursor=conn.cursor()
            query="delete from customer where name=%s"
            value=(self.var_name.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        self.var_name.set("")
        self.var_phone.set("")
        self.var_add.set("")
        self.var_aadhar.set("")
        self.var_licen.set("")
        self.var_email.set("")
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="bike_rental_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+str(self.txt_search.get()))
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
        
        
        
    
    
    
    
        
    
    
