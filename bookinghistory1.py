import tkinter
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector 
from tkinter import messagebox

class bookinghistory(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.root = root
        self.place(x=300, y=0, width=1620, height=1080)

        self.TopImage=PhotoImage (file="top.png") 
        Label(self, image=self.TopImage).place(x=100,y=0)

        self.dockImage=PhotoImage (file="history.png") 
        Label(self, image=self.dockImage, bg="#32405b").place(x=140,y=10)

        self.heading=Label(self, text="Your Order History", font="Courier 20 bold", fg="white",bg="#32405b") 
        self.heading.place( x = 300 , y = 20)

        self.view = Button(self,text="View Booking History",font=("Microsoft YaHei UI light",15),command=self.place_elements)
        self.view.place(x=650,y=10)

        global boxImage
        boxImage = PhotoImage(file="box1.png")

    def place_elements(self):
        con = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
        cursor = con.cursor()
        cursor.execute("SELECT bikeid,models,orderid FROM orders WHERE customerid = 1 ORDER BY orderid")
        data = cursor.fetchall()
        
        step = 150
        y_increment = 0
        for index, row in enumerate(data):
                bikeid = row[0]
                models = row[1]
                orderids=row[2]

                self.bgframe = Frame(self,bg="#546c9c")
                self.bgframe.place(x=10,y=140+y_increment,width=1000,height=90)
                self.text = Label(self, text=f"{models}" , font=("Impact", 20))
                self.text.place(x=10, y=85+y_increment)
            
                self.text1 = Label(self, text="Start date ", font=("Rockwell", 10))
                self.text1.place(x=10, y=118+y_increment)
                
                self.text2 = Label(self.bgframe, text="Do you want to", font=("Rockwell", 13), bg="#546c9c")
                self.text2.place(x=850, y=5)
                self.text3 = Label(self.bgframe, text="renew subscription", font=("Rockwell", 13), bg="#546c9c")
                self.text3.place(x=840, y=29)
            
                
                
                self.label1 = Label(self.bgframe, text="    OWNER    ", font=("Helvetica", 15, 'bold'), fg="white", bg="#546c9c")
                self.label1.place(x=5, y=0)
            
                self.label2 = Label(self.bgframe, text="    PRICE    ", font=("Helvetica", 15, 'bold'), fg="white", bg="#546c9c")
                self.label2.place(x=190, y=0)
            
                self.label3 = Label(self.bgframe, text=" DESCRIPTION ", font=("Helvetica", 15, 'bold'), fg="white", bg="#546c9c")
                self.label3.place(x=340, y=0)
            
                self.label4 = Label(self.bgframe, text="    TYPE    ", font=("Helvetica", 15, 'bold'), fg="white", bg="#546c9c")
                self.label4.place(x=520, y=0)
            

                self.return_button = Button(self.bgframe, text="RETURN", font=("Helvetica", 12, 'bold'), fg="white", bg="#32405b",command=lambda models=models, orderids=orderids: self.open_return_window(models,orderids))                
                self.return_button.place(x=700, y=5)
                
                self.add_review_button = Button(self.bgframe, text="REVIEW", font=("Helvetica", 12, 'bold'), fg="white", bg="#32405b",command=lambda models=models, orderids=orderids: self.open_review_window(models,orderids))
                self.add_review_button.place(x=700, y=50)
                
                self.add_renew_button = Button(self.bgframe, text="RENEW", font=("Helvetica", 12, 'bold'), fg="white", bg="#32405b")
                self.add_renew_button.place(x=880, y=50)
                
                self.owner = Label(self.bgframe, text=f"{bikeid}", font=("Helvetica", 15, 'bold'), fg="black", bg="#546c9c")
                self.owner.place(x=70, y=50)
                
                y_increment += step
            
            
    def open_return_window(self,model,oid):
        return_window = Toplevel(self.root)
        return_window.geometry("300x200")
        return_window.title("Return")
        return_window.configure(bg='#f1edf7')
        ofo = Label(return_window, text=f" {oid} ", font=("Helvetica", 2), fg="#f1edf7")
        ofo.place(x=10, y=10)        
        message = Label(return_window, text=f"Do you want to return {model}", font=("Helvetica", 14))
        message.place(x=20,y=20)
                    
        returnn = Button(return_window, text="RETURN", font=("Helvetica", 12, 'bold'), fg="black", bg="#32405b", command=lambda models=model, oid=oid: self.return_button_click(model,oid))
        returnn.place(x=20, y=60)
        
    def update_order_status(self,model,oid):
        con = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
        cursor = con.cursor()
        cursor.execute("UPDATE orders SET status = 'returned' WHERE models = %s AND orderid = %s;", (model, oid))
        con.commit()
        con.close()
        
    def return_button_click(self,model,oid):
        self.update_order_status(model,oid)
        # Display a message box to confirm that the update was successful
        messagebox.showinfo("You have returned the bike!!", f"We will come tommorow to collect {model}")

            
    def open_review_window(self,model, oid):
        win = Toplevel(self.root)
        win.title("Bike Review")
        win.geometry("500x300+400+50")
        win.resizable(False, False)
        win.configure(bg='#f1edf7')

        momo = Label(win, text=f"Would you like to rate {model} ?", font=("Helvetica", 14))
        momo.place(x=20, y=20)

        oo = Label(win, text=f" {oid} ", font=("Helvetica", 14), fg="#f1edf7")
        oo.place(x=450, y=10)

        def RatingWidget(frame, num_stars=5, size=25, active_color="orange", inactive_color="gray"):
            active_stars = 0
            stars = []

            def draw_widget():
                for i in range(num_stars):
                    star = Label(frame, text="★", font=("Arial", size), fg=inactive_color)
                    star.pack(side=LEFT)
                    star.bind("<Button-1>", lambda e, i=i: set_active_stars(i+1))
                    stars.append(star)

            def set_active_stars(num):
                nonlocal active_stars
                active_stars = num
                for i, star in enumerate(stars):
                    if i < num:
                        star.config(fg=active_color)
                    else:
                        star.config(fg=inactive_color)

            def get_active_stars():
                return active_stars

            draw_widget()

            return get_active_stars

        rating_frame = Frame(win)
        rating_frame.place(x=20, y=45)
        rating_widget = RatingWidget(rating_frame)
        
        revv = Label(win, text=f"Would you like to write a review of {model} ?", font=("Helvetica", 14))
        revv.place(x=20, y=100)

        review_text = StringVar()
        review_text.set("")
        review_entry = Entry(win, width=50, font=("Helvetica", 12), bd=2, relief="groove", textvariable=review_text)
        review_entry.place(x=20, y=130)
        review_text.set("\n\n\n\n")

        def submit_review():
            rating = rating_widget()
            review = review_entry.get()
            try:
                con = mysql.connect(host="localhost", db="minifi", username='root', password='mysql6024', port=3305)
                cursor = con.cursor()
                cursor.execute("INSERT INTO review (reviewid,ratings, reviews, oid, name) VALUES (%s, %s, %s, %s, %s) ", (oid,rating, review, oid,model ))
                con.commit()
                win.destroy()
                messagebox.showinfo("Success", "Review added successfully!")
            except mysql.errors.IntegrityError:
                messagebox.showwarning("Error", "You have already reviewed this product!")
                win.destroy()

        submit_review_button = Button(win, text="SUBMIT", font=("Helvetica", 12, 'bold'), fg="white", bg="#32405b", command=submit_review)
        submit_review_button.place(x=200, y=250)

    
    
        win.mainloop()
    
        

if __name__=='__main__':
    root= Tk()
    
    window = bookinghistory(root)
    root.mainloop()  
