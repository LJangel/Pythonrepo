import csv
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import shutil
from tempfile import NamedTemporaryFile #imported class
from utils.templates import get_template, render_context

#file_item_path = os.path.join(os.getcwd(), "data.csv") #get current working directory for data.csv
file_item_path = os.path.join(os.path.dirname(__file__), "data.csv") #this is a second and better way of doing it
    
host = "smtp.gmail.com"
port = 587
username = "ljmpython@gmail.com"
password = "Zlato1#2013"
from_email = username
to_list = ["box1@toneangel.com"]


class UserManager():
    def render_message(self, user_data):
        file_ = "templates/email_messages.txt"
        file_html = "templates/email_messages.html"
        template = get_template(file_)
        template_html = get_template(file_html)
        if isinstance(user_data, dict): #is a dictionary
            context = user_data
            plain_ = render_context(template, context)
            html_ = render_context(template_html, context)
            return (plain_, html_) #underscores used so that they are known as a variable
        return (None, None) #tuple

    def message_user(self, user_id=None, email=None, subject="Billing Update!"):
        user = self.get_user_data(user_id=user_id, email=email)
        if user:
            plain_, html_ = self.render_message(user)
            print(plain_, html_)
            user_email = user.get("email", "box1@toneangel.com") #get the email if in dictionary, otherwise use box1 address
            to_list.append(user_email)
            try:                
                email_conn = smtplib.SMTP(host, port)
                email_conn.ehlo()
                email_conn.starttls()
                email_conn.login(username, password)
                the_msg = MIMEMultipart("alternative")
                the_msg['Subject'] = subject
                the_msg["From"] = from_email
                the_msg["To"]  = user_email
                part_1 = MIMEText(plain_, 'plain')
                part_2 = MIMEText(html_, 'html')
                the_msg.attach(part_1)
                the_msg.attach(part_2)
                email_conn.sendmail(from_email, to_list, the_msg.as_string())
                email_conn.quit()
            except smtplib.SMTPException:
                print("error sending message")
        return None

    def get_user_data(self, user_id=None, email=None):  #this was previously "read_data" in other files
        filename = file_item_path
        #print(file_item_path)
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            items = []
            unknown_user_id = None #must declare these before use due to if statements
            unknown_email = None
            for row in reader:
                if user_id is not None: #is not None is a good idea in case you have a default above in the definition of the function
                    if int(user_id) == int(row.get("id")):
                        return row
                    else:
                        unknown_user_id = user_id
                if email is not None:
                    if email == row.get("email"):
                        return row
                    else:
                        unknown_email = email
            if unknown_user_id is not None:
                print("User id {user_id} not found".format(user_id=user_id))
            if unknown_email is not None:
                print("Email {email} not found".format(email=email))
        return None #if both user_id and email are blank it will return nothing
