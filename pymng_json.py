import json
import pymongo
myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = myclient["mydatabase"]
mycol1 = mydb["restaurants"]
file = open("/home/tibil/Downloads/restaurants.json","r")
reader = json.load(file)
#mydb.restaurants.drop()
#mydb.restaurants.insert(reader)
#mydb.fire_json.insert_one(reader)'borough': 'Bronx'
#query = {"grades" : { "$elemMatch":{"score":{"$gt" : 20,"$lt":50}}}}
query = {"address.coord":{"$lt":-50.754168}}
query ={"grades.score":{"$gt":20}}
query = {"cuisine" : {"$nin":["American "]},"grades.score":{"$gt":40},"address.coord":{"$lt":-50.754168}}
query = {"cuisine" : {"$nin":["American "]},"grades.grade":"A","borough" : {"$nin":["Brooklyn"]}}
#x = mydb.restaurants.find(query).sort("cuisine",-1)
#x = mydb.restaurants.find({},{'_id':0,"restaurant_id":1,"name":1,"borough":1,"address.zipcode":1})
query = {"name":{"$regex":"Wil"}}
#x = mydb.restaurants.find(query,{"_id":0,"restaurant_id":1,"name":1,"borough":1,"cuisine":1})
query = {"name":{"$regex":"Reg"}}
#x = mydb.restaurants.find(query,{"_id":0,"restaurant_id":1,"name":1,"borough":1,"cuisine":1})
query = {'borough': 'Bronx','cuisine': {"$in":['American ','chinese']}}
query = {'borough':{"$nin":['Staten Island','Queens','Bronx','Brooklyn']}}
query = {"grades.score":{"$lt":10}}
query = {"cuisine":{"$nin":["American ","chinees"]}}
#x = mydb.restaurants.find(query,{"_id":0,"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"grades.score":1})
query ={"grades.grade":"A","grades.score":11,"grades.date":"ISODate(2014-08-11T00:00:00Z)"}
x = mydb.restaurants.find(query,{"_id":0,"restaurant_id":1,"name":1,"grades.grade":1})
print(x.count())
for a in x:
    print(a)