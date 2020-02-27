import pymongo
import csv
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = myclient["mydatabase"]
mycol = mydb['fire']
myfile = open("/home/tibil/Downloads/Fire_Incidents_Data.csv","r")
reader = csv.DictReader(myfile)
header = ['Incident_Number', 'Exposure Number', 'Address', 'Incident Date', 'Call Number', 'Alarm DtTm', 'Arrival DtTm', 'Close DtTm', 'City', 'Zipcode', 'Battalion', 'Station Area', 'Box', 'Suppression Units', 'Suppression Personnel', 'EMS Units', 'EMS Personnel', 'Other Units', 'Other Personnel', 'First Unit On Scene', 'Estimated Property Loss', 'Estimated Contents Loss', 'Fire Fatalities', 'Fire Injuries', 'Civilian Fatalities', 'Civilian Injuries', 'Number of Alarms', 'Primary Situation', 'Mutual Aid', 'Action Taken Primary', 'Action Taken Secondary', 'Action Taken Other', 'Detector Alerted Occupants', 'Property Use', 'Area of Fire Origin', 'Ignition Cause', 'Ignition Factor Primary', 'Ignition Factor Secondary', 'Heat Source', 'Item First Ignited', 'Human Factors Associated with Ignition', 'Structure Type', 'Structure Status', 'Floor of Fire Origin', 'Fire Spread', 'No Flame Spead', 'Number of floors with minimum damage', 'Number of floors with significant damage', 'Number of floors with heavy damage', 'Number of floors with extreme damage', 'Detectors Present', 'Detector Type', 'Detector Operation', 'Detector Effectiveness', 'Detector Failure Reason', 'Automatic Extinguishing System Present', 'Automatic Extinguishing Sytem Type', 'Automatic Extinguishing Sytem Perfomance', 'Automatic Extinguishing Sytem Failure Reason', 'Number of Sprinkler Heads Operating', 'Supervisor District', 'Neighborhood_District', 'Location', '']
# for each in reader:
#     row = {}
#     for field in header:
#         row[field] = each[field]
#     mydb.mycol.insert(row)
#x = mycol.insert_many(myfile)
#x = mydb.mycol.find({},{'Incident_Number':1,'Exposure Number':1})
#query = {'Neighborhood_District': 'Marina'}
# query = {'Neighborhood_District': {"$gt":"S"}}
query = {'Neighborhood_District': {"$regex":"^M"}}
x = mydb.mycol.find().pretty()
for a in x:
    print(a)

