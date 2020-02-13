import mysql.connector  as con
import json


mydb = con.connect(
  host="localhost",
  user="root",
  passwd="MYSQL123",
  db="demo"
)
cur=mydb.cursor()

cur.execute("select name from json_to_db ")

res=cur.fetchall()
print(res)

li=list()
for i in res:
  li.append(' '.join(i))


print(li)

mydict=dict()
for word in li:
  if word not in mydict:
    mydict[word]=1
  else:
    mydict[word]+=1
print(mydict)

x=json.dumps(mydict)
print(x)