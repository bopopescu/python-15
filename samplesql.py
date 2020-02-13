import mysql.connector as con


mydb = con.connect(
  host="localhost",
  user="root",
  passwd="MYSQL123",
  db="demo"
)


cur=mydb.cursor()
f=open("myfile.sql","r")
fh = f.readline()


# sql_query  = "create table if not exists mytable(properties varchar(20) , python varchar(20), java varchar(20), C varchar(20))"
for x in f:
    cur.execute(x)
    mydb.commit()
# cur.execute(f.readline())
# mydb.commit()

