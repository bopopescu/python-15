mylist=[ {
    "ID": "2",
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
  },{
    "ID": "2",
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
  }]
for x in mylist:
    print(x)
for mydict in mylist:
    columns=",".join(""+str(x).replace('/','_')+"" for x in mydict.keys())
    values=",".join("'"+str(x).replace('/','_')+"'" for x in mydict.values())
    sql="INSERT INTO %s (%s) VALUES (%s);"%('mytable',columns,values)
    print(sql)
