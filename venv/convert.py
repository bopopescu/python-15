import json
import csv
f=open("driver.json")
data=json.load(f)
f.close()

f=open("driver1.csv")
csvfile=csv.writer(f)
for item in data:
    f.writelines(item)
f.close()
