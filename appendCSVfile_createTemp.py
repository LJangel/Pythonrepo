import csv
import shutil
from tempfile import NamedTemporaryFile #imported class
# these are all built in functions in Python

#figure out the number of rows
def get_length(file_path):
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)  #lists the contents so the length can be determined  
    return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ["id", "name", "email"]
    #the number of rows?
    next_id = get_length(file_path)
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()  not needed
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
            })
    
#append_data("data.csv", "Larry", "box1@toneangel.com")
# if data.csv is not in the same directory, the whole path is needed above

filename = "data.csv"
temp_file = NamedTemporaryFile(delete=False)

with open(filename, "rb") as csvfile, temp_file:  #rb is read binary
    reader = csv.DictReader(csvfile)
    fieldnames = ["id", "name", "email", "amount", "sent"]
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        print(row)  #to see that each row is a dictionary value
        writer.writerow({
            "id": row["id"],  #can do it this way because the reader reads these from the existing csv file rows
            "name": row["name"],
            "email": row["email"],
            "amount": "1293.23",
            "sent": "",
            })
    
    #shutil.move(temp_file.name, filename) #moves the data to the new file
