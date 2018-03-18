import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile #imported class
# these are all built in functions in Python

#figure out the number of rows
def get_length(file_path):
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)  #lists the contents so the length can be determined  
    return len(reader_list)

def append_data(file_path, name, email, amount, sent):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    #the number of rows?
    next_id = get_length(file_path)
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()  #not needed
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
            "amount": amount,
            "sent": "",
            "date": datetime.datetime.now()
            })
    
#append_data("data.csv", "Larry", "box1@toneangel.com", 123.22, "")
#if data.csv is not in the same directory, the whole path is needed above

def edit_data(edit_id=None, email=None, amount=None, sent=None):
    filename = "data.csv"
    temp_file = NamedTemporaryFile(mode='w+', delete=False, newline="")
    with open(filename, 'r', newline="") as csvfile, temp_file: 
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        #print(temp_file.name)
        for row in reader:
            if edit_id is not None:
                if int(row['id']) == int(edit_id):  #to make sure rows are counted as ints
                    row['amount'] = amount
                    row['sent'] = sent
            elif email is not None and edit_id is None:
                if str(row['email']) == str(email):  
                    row['amount'] = amount
                    row['sent'] = sent
                print(row)
            else:
                pass
            writer.writerow(row)                        
            shutil.move(temp_file.name, filename)#moves the data to the new file        
        return True #return True if it doesn't what it's supposed to
    return False #return False if it fails


edit_data(email="box1@toneangel.com", amount=99.99, sent="")