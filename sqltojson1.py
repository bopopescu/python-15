import itertools

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
cur.execute("select Incident_Number from demo1 where Call_Type='Medical Incident'")
res1 = cur.fetchall()
print(sum(res1,()))
out = list(sum(res1, ()))
# out = list(itertools.chain(*res1))
print(out)
# res1 = [item for t in res1 for item in t]
# lst1 = list()
# print(res1)
# for x in res1:
#     print(x)
# cur.execute("select Incident_Number from demo1 where Call_Type='Alarms'")
# res = cur.fetchall()
# lst2 = list(res)
# # print(lst2)
# cur.execute("select Incident_Number from demo1 where Call_Type='Citizen Assist / Service Call'")
# res = cur.fetchall()
# lst3 = list(res)
# #print(lst3)
# cur.execute("select Incident_Number from demo1 where Call_Type='Traffic Collision'")
# res = cur.fetchall()
# lst4 = list(res)
# #print(lst4)
# cur.execute("select Incident_Number from demo1 where Call_Type='Other'")
# res = cur.fetchall()
# lst5 = list(res)
# #print(lst4)
# cur.execute("select Incident_Number from demo1 where Call_Type='Outside Fire'")
# res = cur.fetchall()
# lst6 = list(res)
# #print(lst4)
# cur.execute("select Incident_Number from demo1 where Call_Type='Structure Fire'")
# res = cur.fetchall()
# lst7 = list(res)
# #print(lst4)
# cur.execute("select Incident_Number from demo1 where Call_Type='Elevator / Escalator Rescue'")
# res = cur.fetchall()
# lst8 = list(res)
# #print(lst4)
# cur.execute("select Incident_Number from demo1 where Call_Type='Vehicle Fire'")
# res = cur.fetchall()
# lst9 = list(res)
# #print(lst4)
# cur.execute("select Incident_Number from demo1 where Call_Type='Gas Leak (Natural and LP Gases)'")
# res = cur.fetchall()
# lst10 = list(res)
# #print(lst4)
# d1 = dict()
# d1["Medical Incident"] = res1
# d1["Alarms"] = lst2
# d1["Citizen Assist / Service Call"] = lst3
# d1["Traffic Collision"] = lst4
# d1["Other"] = lst5
# d1["Outside Fire"] = lst6
# d1["Structure Fire"] = lst7
# d1["Elevator / Escalator Rescue"] = lst8
# d1["Vehicle Fire"] = lst9
# d1["Gas Leak (Natural and LP Gases)"] = lst10
#
# d2 = dict()
# d2["Call_Type"] = d1
# d3 = dict()
# d3["Fire_Details"] = d2
# print(d3)
#
# with open("fire.json",'w') as jsonfile:
#     jsonfile.write(json.dumps(d3,indent=4))
#
# csv_o = open("fire.csv", 'w')
# csv_w = csv.writer(csv_o)
#
# csvdata = d1["Medical Incident"]
# count = 0
# for data in csvdata:
#     if count == 0:
#         head = d1.keys()
#         csv_w.writerow(head)
#         count += 1
#     csv_w.writerow(d1.values())