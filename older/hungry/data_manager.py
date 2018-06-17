import csv
import datetime
import os
import shutil
from tempfile import NamedTemporaryFile #imported class
# these are all built in functions in Python

#file_item_path = os.path.join(os.getcwd(), "data.csv") #get current working directory for data.csv
file_item_path = os.path.join(os.path.dirname(__file__), "data.csv") #this is a second and better way of doing it

def read_data(user_id=None, email=None):
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
            return "User id {user_id} not found".format(user_id=user_id)
        if unknown_email is not None:
            return "Email {email} not found".format(email=email)
    return None #if both user_id and email are blank it will return nothing
