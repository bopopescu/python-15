import mysql.connector  as con
import json
import csv


mydb = con.connect(
  host="localhost",
  user="root",
  passwd="MYSQL123",
  db="demo"
)
cur=mydb.cursor()

cur.execute("select * from json_to_db ")

res=cur.fetchall()
for x in res:
    print(x)
print(res)
li=[]
for x,y in res:
    li.append(x)
print(li)
d0={}
for word in li:
    if word not in d0:
        d0[word]=1
    else:
        d0[word]+=1
print(d0)
li2=list(d0.keys())
li2.sort()
print("mine ",li2)

# for x in d0:
#     li2.append(x)
# print(li2)
print(sorted(li2))
d=dict()
for a,b in res:
    d[a]=b
print(d)
d1={}

d1["Names"]=d
print(d1)
d1["Count"]=d0

with open("file.json",'w') as jsonfile:
    jsonfile.write(json.dumps(d1,indent=4))

csv_o=open("file.csv",'w')
csv_w=csv.writer(csv_o)

csvdata=d1["Names"]
count=0
for data in csvdata:
    if count==0:
        head=d.keys()
        csv_w.writerow(head)
        count+=1
    csv_w.writerow(d.values())

