import tkinter as tk
import mysql.connector 
from PIL import ImageTk, Image
import io
from tkinter import messagebox
import smtplib
import os
from email.message import EmailMessage
import ssl
import smtplib

class BikeRentalApp:
    def __init__(self, root):
        # Create the main window
        self.root = root
        self.root.configure(bg="purple")

        # Create a database connection
        self.conn = mysql.connector.connect(host="localhost",database="bike_rental_database",user="root",password="root")
        self.cursor = self.conn.cursor()

        # Create a frame for the application list
        self.application_frame = tk.Frame(root, bg="purple")
        self.application_frame.pack()

        # Display the initial list of applications
        self.update_application_list()

    # Define a function to retrieve the updated list of applications from the database
    def get_approvals(self):
        self.cursor.execute("SELECT * FROM approval ")
        approvals = self.cursor.fetchall()
        return approvals

    # Define a function to approve the application
    '''def approve_application(self, bikeid, bike_name, mileage, engine, front, rear, displacement, fuel_capacity, body_type, speedometer, odometer, image_data, owner):
        try:
            # Insert the application data into the bikes table
            self.cursor.execute("INSERT INTO bikes (bikeid, bikename, mileage, engine, front, rear, displacement, fuelcapacity, bodytype, speedometer, odometer, bikeimage, owner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (bikeid, bike_name, mileage, engine, front, rear, displacement, fuel_capacity, body_type, speedometer, odometer, image_data, owner))
            self.conn.commit()

            # Delete the application from the approvals table
            self.cursor.execute("DELETE FROM approval WHERE bikeid=%s", (bikeid,))
            self.conn.commit()

            # Update the application list
            self.update_application_list()
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((400,300))
            photo_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo_image)
            self.image_label.image = photo_image

        except mysql.connector.Error as error:
            print("Error approving application:", error)'''
    def approve_application(self, bikeid, bike_name, mileage, engine, front, rear, displacement, fuel_capacity, body_type, speedometer, odometer, image_data, owner,category):
        try:
        # Create a new window for entering hourly rate and monthly subscription rate
            new_window = tk.Toplevel(self.root)
            new_window.configure(background='purple')

            # Add labels and entry fields for hourly rate and monthly subscription rate
            hourly_label = tk.Label(new_window, text="Hourly Rate:",bg='purple', fg='white')
            hourly_label.pack(pady=10)

            hourly_entry = tk.Entry(new_window)
            hourly_entry.pack()

            monthly_label = tk.Label(new_window, text="Monthly Subscription:",bg='purple', fg='white')
            monthly_label.pack(pady=10)

            monthly_entry = tk.Entry(new_window)
            monthly_entry.pack()
            
            
            # Add a submit button that inserts all values into the bikes database, including hourly rate and monthly subscription rate
            submit_button = tk.Button(new_window, text="Submit", bg='black', fg='white', command=lambda: self.insert_bike_data(bikeid, bike_name, mileage, engine, front, rear, displacement, fuel_capacity, body_type, speedometer, odometer, image_data, owner, hourly_entry.get(), monthly_entry.get(),category, new_window))
            submit_button.pack(pady=20)
            
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((400, 300))
            self.photo_image = ImageTk.PhotoImage(image)

        # Add label for displaying image
            self.image_label = tk.Label(new_window, image=self.photo_image)
            self.image_label.pack()


        except mysql.connector.Error as error:
            print("Error approving application:", error)


    def insert_bike_data(self, bikeid, bike_name, mileage, engine, front, rear, displacement, fuel_capacity, body_type, speedometer, odometer,image_data, owner, hourly_rate, monthly_subscription,category, window):
        try:
            # Insert the bike data into the bikes table, including hourly rate and monthly subscription rate
            self.cursor.execute("INSERT INTO bikes (bikename, mileage, engine, front, rear, displacement, fuelcapacity, bodytype, speedometer, odometer,bikeimage,category, owner, hourlyrate, monthlyrate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)", (bike_name, mileage, engine, front, rear, displacement, fuel_capacity, body_type, speedometer, odometer,image_data,category, owner, hourly_rate, monthly_subscription))
            self.conn.commit()

            # Delete the application from the approvals table
            self.cursor.execute("DELETE FROM approval WHERE bikeid=%s", (bikeid,))
            self.conn.commit()

            self.cursor.execute("SELECT email from customers where fname=%s",(owner,))
            row=self.cursor.fetchone()
            emailid=row[0]
            # Update the application list
            self.update_application_list()
            #image = Image.open(io.BytesIO(image_data))
            #image = image.resize((400,300))
            #photo_image = ImageTk.PhotoImage(image)
            #self.image_label.config(image=photo_image)
            #self.image_label.image = photo_image
            messagebox.showinfo("Success","Bike Approved and added to the database")
            email_sender = 'vesitbikerentalsystem@gmail.com'
            email_password= 'tfzcclyabdovxfeo'
            email_receiver = emailid

            subject = "Your Bike has been approved"
            body = """
            Your Bike has been successfully approved and now can be used by other users for rental.
            We will soon come to pick up your Bike.
            Following are your bike details\n
                """+"Bike Name: "+bike_name+"\tMileage: "+str(mileage)+"\nEngine: "+engine+"\n\nThank you"

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                    smtp.login(email_sender,email_password)
                    smtp.sendmail(email_sender,email_receiver,em.as_string())

            messagebox.showinfo("Success","Email Sent to User")
            # Close the window
            window.destroy()

        except mysql.connector.Error as error:
            print("Error inserting bike data:", error)

    # Define a function to deny the application
    def deny_application(self, bikeid):
        try:
            self.cursor.execute("DELETE FROM approval WHERE bikeid=%s", (bikeid,))
            self.conn.commit()
            self.update_application_list()
        except mysql.Error as error:
            print("Error deleting approval:", error)

    # Define a function to update the application list
    def update_application_list(self):
        # Clear the existing labels
        for widget in self.application_frame.winfo_children():
            widget.destroy()

        # Retrieve the updated list of applications
        approvals = self.get_approvals()

        # Create a label for each application
        for approval in approvals:
            label_text = f"Bike ID: {approval[0]}\nBike Name: {approval[1]}\nMileage: {approval[2]}\nEngine: {approval[3]}\nFront: {approval[4]}\nRear: {approval[5]}\nDisplacement: {approval[6]}\nFuel Capacity: {approval[7]}\nBody Type: {approval[8]}\nSpeedometer: {approval[9]}\nOdometer: {approval[10]}\nOwner Name: {approval[12]}"
            label = tk.Label(self.application_frame, text=label_text, bg="black", fg="white", font=("Arial", 10))
            label.pack(pady=10)
            global category
            category=approval[13]
            # Create buttons for approving or denying the application
            button_frame = tk.Frame(self.application_frame, bg="black")
            approve_button = tk.Button(button_frame, text="Approve", bg="black", fg="white", font=("Arial", 10), command=lambda bikeid=approval[0], data=approval[1:]: self.approve_application(bikeid, *data))
            approve_button.pack(side="left", padx=5, fill='both', expand=True)
            deny_button = tk.Button(button_frame, text="Deny", bg="black", fg="white", font=("Arial", 10), command=lambda bikeid=approval[0]:self.deny_application(bikeid))
            deny_button.pack(side="left", padx=5, fill='both', expand=True)
            button_frame.pack()

    
    # Configure the application frame to have a purple background and white text
    

# Create the main window




# Start the event loop


# Close the database connection

        
if __name__ == "__main__":
    root = tk.Tk()
    app = BikeRentalApp(root)
    root.mainloop()
