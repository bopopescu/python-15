import pyspark
from pyspark.shell import spark
from pyspark.sql import functions as F
from pyspark.sql.types import *
#sqlContext = SQLContext(sc)
df = spark.read.load('/home/tibil/Downloads/Fire_Department_Calls.csv',
                          format ='csv',
                          header ='true',
                          inferSchema ='true')
df2 = spark.read.load('/home/tibil/Downloads/Fire_Incidents_Data.csv',
                      format ='csv',
                      header = 'true',
                      inferschema = 'true')
print(df.show(10))
print(df.count())
print(df.select('Call_Type').distinct().show())
df.select('Call Date','Call_Type').distinct().filter((df['Call_Type']).endswith('Fire')).show(1000)
#print(df.describe.show())
print(df.groupBy('Call_Type').count().orderBy('count',ascending = False).show(10))
print(df.select(F.countDistinct('Call_Type')).show())
df3 = df.join(df2,on=['Incident_Number'],how='inner')
print(df3.select('Call_Type','Neighborhood_District').filter((df3['Neighborhood_District']).contains('Nob Hill')).show(100))
print(df3.select('Call_Type','Neighborhood_District').show())