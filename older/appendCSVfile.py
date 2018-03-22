import csv

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
    
append_data("data.csv", "Larry", "box1@toneangel.com")
# if data.csv is not in the same directory, the whole path is needed above

