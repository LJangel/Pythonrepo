import csv

with open("data.csv", "w+", newline='') as csvfile: #I found newline in documentation to avoid auto add of blank line
...     writer = csv.writer(csvfile)
...     writer.writerow(["Title", "Description", "Col 3"])
...     writer.writerow(["Row 1", "Some Desc", "another"])
...     writer.writerow(["Row 1", "Some Desc", "another"])

with open("data.csv", "a", newline="") as csvfile: #appends
...     writer = csv.writer(csvfile)
...     writer.writerow(["append row", "Some Desc", "another"])

with open("data.csv", "r", newline="") as csvfile: #reads only
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

""" w+ is a mode that allows read, 
write and overwrite of existing file or creates new file
"""


#using a dictonary instead of a list is better-
with open("data.csv", "r", newline="") as csvfile: #reads only
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


with open("data.csv", "a", newline="") as csvfile: #appends
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
    writer.writerow({"id":123, "title": "new title"})

#next one will overwrite the file and will add the header row
with open("data.csv", "w", newline="") as csvfile: #appends
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()    
    writer.writerow({"id":123, "title": "new title"})