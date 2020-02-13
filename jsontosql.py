import json
f=open("driver.json","r")
data=json.load(f)
print(data)
import mysql.connector as con
db=con.connect(
    host="localhost",
    user="root",
    password="MYSQL123"
    ,db="demo")
cur=db.cursor()
cur.execute("create table if not exists language (properties varchar(20),python varchar(20),java varchar(20),C varchar(20))")
item=data.items()
i=0
for a,b in item:
    while i<len(b):
        pr=b[i]['properties']
        py=b[i]['python']
        ja=b[i]['java']
        c=b[i]['C']
        sql="insert into language values(%s,%s,%s,%s)"
        val=(pr,py,ja,c)
        cur.execute(sql,val)
        i+=1
        db.commit()