import mysql.connector as con
from pyspark import SparkContext
import json
import csv

mydb = con.connect(
    host = "localhost",
    user = "root",
    password = "MYSQL123",
    db = "psdb"
)
cur = mydb.cursor()
cur.execute("select * from demo1")
res1 = cur.fetchall()
sc = SparkContext("local","sparkC")
words = sc.parallelize(res1)
words_filter = words.filter((lambda x:'Incident' in x))
filtered = words_filter.collect()
print(filtered)