import smtplib
import os
import time
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime

def send_email():
    # Set up the email parameters
    sender_email = 'senders-email@gmail.com'
    sender_password = 'put-senders password'
    receiver_email = 'receivers-email@gmail.com'
    subject = 'Attendance Sheet'
    body = 'Please find attached the attendance sheet for today.'

    # Set up the Excel sheet attachment
    now = datetime.now()
    day_of_week = now.strftime("%A")
    time_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"attendance_{day_of_week}_{time_string}.xlsx"
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='xlsx')
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    if os.path.exists(filename):
        message.attach(attachment)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Send the latest attendance sheet and exit
send_email()
