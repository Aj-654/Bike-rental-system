import tkinter as tk
import smtplib
import os
from email.message import EmailMessage
import ssl
import smtplib

class sendemail:
    def __init__(self):
        email_sender = 'vesitbikerentalsystem@gmail.com'
        email_password= 'tfzcclyabdovxfeo'
        email_receiver = '2021.ishwari.datir@ves.ac.in'

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
