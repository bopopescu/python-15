import json
pyfile=open('/home/tibil/a1.json','r')
pydata=json.load(pyfile)

import mysql.connector

db =mysql.connector.connect(host = 'localhost',user ='root',passwd='MYSQL123',db='demo')
cur=db.cursor()
cur.execute("create table if not exists json_to_db(name varchar(20), phno varchar(20))")

item=pydata.items()
global i
i=0
for a,b in item:
   while i < len(b):
        na=b[i]['name']
        ph=b[i]['phno']
        sql = "insert into json_to_db values(%s,%s)"
        val = (na,ph)
        cur.execute(sql,val)
        i+=1
        db.commit()

# mylist=list(f)
# for mydict in mylist:
#     columns=",".join(""+str(x).replace('/','_')+"" for x in mydict.keys())
#     values=",".join("'"+str(x).replace('/','_')+"'" for x in mydict.values())
#     sql="INSERT INTO %s (%s) VALUES (%s);"%('mytable',columns,values)
#     print(sql)