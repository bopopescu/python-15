import json
"""f=open("std1","r")
mylist=[ {"ID": "1",
    "Name": "Senpai",
    "Gender": "1",
    "Class": "32",
    "Seat": "15",
    "Club": "0",
    "Persona": "1",
    "Crush": "0",
    "BreastSize": "0",
    "Strength": "0",
    "Hairstyle": "1",
    "Color": "Black",
    "Eyes": "Black",
    "EyeType": "Default",
    "Stockings": "None",
    "Accessory": "0",
    "ScheduleTime": "7_7_8_13.01_13.375_15.5_16_17.25_99_99",
    "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Hangout_Locker_Exit",
    "ScheduleAction": "Stand_Stand_Read_Sit_Eat_Sit_Clean_Read_Shoes_Stand",
    "Info": "An average student.Average grades, average looks, average life..."
  },
  {"ID": "2",
    "Name": "Yui Rio",
    "Gender": "0",
    "Class": "11",
    "Seat": "14",
    "Club": "1",
    "Persona": "5",
    "Crush": "0",
    "BreastSize": "0.5",
    "Strength": "0",
    "Hairstyle": "2",
    "Color": "Red",
    "Eyes": "Red",
    "EyeType": "Default",
    "Stockings": "Red",
    "Accessory": "0",
    "ScheduleTime": "7_7_8_13_13.375_15.5_16_17.25_99_99",
    "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Club_Locker_Exit",
    "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_SocialSit_Shoes_Stand",
    "Info": ""
  }
   ]



for mydict in mylist:
    columns=",".join(""+str(x).replace('/','_')+"" for x in mydict.keys())
    values=",".join("'"+str(x).replace('/','_')+"'" for x in mydict.values())
    sql="INSERT INTO %s (%s) VALUES (%s);"%('student1',columns,values)
    #print(sql)

    f=open("student.sql","a")
    f.write(sql +"\n")"""
import mysql.connector as con


mydb = con.connect(
  host="localhost",
  user="root",
  passwd="MYSQL123",
  db="demo"
)


cur=mydb.cursor()
f=open("student.sql","r")
fh = f.readline()


#sql_query  = "create table if not exists student1(ID varchar(20),Name varchar(20),Gender varchar(20),Class varchar(20),Seat varchar(20),Club varchar(20),Persona varchar(20),Crush varchar(20),BreastSize varchar(20),Strength varchar(20),Hairstyle varchar(20),Color varchar(20),Eyes varchar(20),EyeType varchar(20),Stockings varchar(20),Accessory varchar(20),ScheduleTime varchar(200),ScheduleDestination varchar(200),ScheduleAction varchar(200),Info varchar(200))"
#cur.execute(sql_query)
for x in f:
    cur.execute(x)
    mydb.commit()
# cur.execute(f.readline())
# mydb.commit()

