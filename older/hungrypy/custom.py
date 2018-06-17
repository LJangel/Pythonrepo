import smtplib


host = "smtp.gmail.com"
port = 587
username = "ljmpython@gmail.com"
password = "Zlato1#2013"
from_email = username
to_list = ["box1@toneangel.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo() # says hello to the gmail server
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello there this is an email message")
email_conn.quit() #ends connection

#another way of doing it
from smtplib import SMTP #this is a built in class in smtplib (see documentation online)
email_conn2 = SMTP(host, port)
email_conn2.ehlo() # says hello to the gmail server
email_conn2.starttls()
email_conn2.login(username, password)
email_conn2.sendmail(from_email, to_list, "Hello there this is an email message")
email_conn2.quit() #ends connection

#deal with exceptions from server (copied from documentation)
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host, port)
pass_wrong.ehlo() # says hello to the gmail server
pass_wrong.starttls()
try:            #allows exception handling
    pass_wrong.login(username, "wrong_password")
    pass_wrong.sendmail(from_email, to_list, "Hello there this is an email message")
except SMTPAuthenticationError:
    print("Could not log in")
except: 
    print("an error occured")
pass_wrong.quit() #ends connection


