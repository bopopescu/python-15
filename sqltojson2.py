import mysql.connector as con
import json
import csv

mydb = con.connect(
    host = "localhost",
    user = "root",
    password = "MYSQL123",
    db = "psdb"
)
cur = mydb.cursor()
cur.execute("select * from demo1")
res1 = cur.fetchall()
print(res1)
# l1=[]
# l2=[]
l1,l2,l3,l4,l5,l6,l7,l8=([] for i in range(8))
for x,y in res1:
    if x =="Medical Incident":
        l1.append(y)
    elif x == "Other":
        l2.append(y)
    elif x == "Alarms":
        l3.append(y)
    elif x=="Citizen Assist / Service Call":
        l4.append(y)
    elif x=="Traffic Collision":
        l5.append(y)
    elif x=="Outside Fire":
        l6.append(y)
    elif x=="Structure Fire":
        l7.append(y)
    elif x=="Elevator / Escalator Rescue":
        l8.append(y)
d1=dict()
d1["Medical Incident"]=l1
d1["Other"]=l2
d1["Alarms"]=l3
d1["Citizen Assist / Service Call"]=l4
d1["Traffic Collision"]=l5
d1["Outside Fire"]=l6
d1["Structure Fire"]=l7
d1["Elevator / Escalator Rescue"]=l8
d2=dict()
d2["Call_Type"]=d1
d3=dict()
d3["Fire_Details"]=d2
print(d3)

with open("fire1.json","w") as jsonfile:
    jsonfile.write(json.dumps(d3,indent=4))