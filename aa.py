import csv,json
csvfilepath="data.csv"
jsonfilepath="driver.json"

data={}
with open(csvfilepath) as csvfile:
    csvreader=csv.DictReader(csvfile)
    for rows in csvreader:
        id=rows["Programming language"]
        data[id]=rows
with open(jsonfilepath,'w') as jsonfile:
    jsonfile.write(json.dumps(data,indent=4))
