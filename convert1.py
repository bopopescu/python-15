import json
import csv


inputfile=open("student.json")
data=json.load(inputfile)
print(data)


prog_data = data["details"]

csv_openin = open("students.csv",'w')
cvw_writing = csv.writer((csv_openin))

count = 0

for data in prog_data:
    if count == 0 :
        head = data.keys()
        cvw_writing.writerow(head)
        count += 1
    cvw_writing.writerow(data.values())






for k in data:
    output.writerow(k.values())

