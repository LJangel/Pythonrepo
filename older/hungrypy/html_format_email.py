from email.mime.multipart import MIMEMultipart #allows html email format
from email.mime.text import MIMEText #fallback plain text format
import smtplib
#note, always put imports in alphabetical order
#email is another built in python module

host = "smtp.gmail.com"
port = 587
username = "ljmpython@gmail.com"
password = "Zlato1#2013"
from_email = username
to_list = ["box1@toneangel.com"]

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo() # says hello to the gmail server
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg = MIMEMultipart("alternative") #this is a standard way of sending
    the_msg["Subject"] = "Hello there!"
    the_msg["From"] = from_email
    #the_msg["To"] = to_list[0] #references first item in the list
    
    plain_txt = "Testing the message"
    html_txt = """\
    <html>
        <head></head>
        <body>
            <p>Hey!<br/>
            Testing this email <b>message</b>.  Made by <a ref='http://joincfe.com'>Team CFE</a>.
            </p>
        </body>
    </html>
    """
    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')
    
    the_msg.attach(part_1)
    the_msg.attach(part_2)
#print(the_msg.as_string()) #to view it an make sure it's right
    
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit() #ends connection
except smtplib.SMTPException:
    print("error sending message")
