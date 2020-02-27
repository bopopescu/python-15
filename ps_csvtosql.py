#import py2jdbc
# from pyspark import SparkContext
#import mysql.connector
#from pyspark.shell import spark
from pyspark.sql import SparkSession
spark = SparkSession\
     .builder\
     .appName("Pyspark SQL")\
     .config("spark,some.config.option","some-value")\
     .getOrCreate()

# df = spark.read.csv("/home/tibil/Downloads/Fire_Department_Calls.csv",
#                     inferSchema=True,
#                     header=True)
# df1 = df.select('Call_Type').distinct()
# print(df1)

# df1.write.format('jdbc').options(url='jdbc:mysql://localhost:3306/psdb',
#                         driver='com.mysql.jdbc.Driver',
#                         dbtable="demo1",
#                         user='root',
#                         password='MYSQL123').mode('append').save()

spark.read.format("jdbc")\
    .options(url="jdbc:mysql://localhost:3306/psdb") \
    .options(driver="com.mysql.jdbc.Driver") \
    .options(dbtable='demo') \
    .options(user="root") \
    .options(password="MYSQL123").load().show()

print("success")
# df1.write.jdbc(url="jdbc:mysql://localhost:3306/psdb"
#                     "?user=root&password=MYSQL123",
#                 table="demo1",
#                 mode="append",
#                 properties={"driver": 'com.mysql.jdbc.Driver'})
#spark.read.format("jdbc").option("url",'jdbc:mysql://localhost:3306/psdb').option("dbtable","demo").option("driver",'com.mysql.jdbc.Driver').load().show()
#spark.read.format("jdbc").option("url",'jdbc:mysql://localhost:3306/psdb').option("dbtable","demo").load().show()
print("success")