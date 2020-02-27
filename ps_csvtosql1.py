from pyspark import SparkContext as sc
from pyspark.sql import SparkSession
spark = SparkSession\
    .builder\
    .appName("Python Spark SQL basic example")\
    .config("Spark.some.config.option","Some-value")\
    .getOrCreate()

df=spark.read.csv("/home/tibil/Downloads/Fire_Department_Calls.csv", inferSchema=True, header=True)
df1=df.select('Call_Type','Incident_Number').distinct()
print(df1)

df1.write.format('jdbc').options(url='jdbc:mysql://localhost:3306/psdb',
                         driver='com.mysql.cj.jdbc.Driver',
                         dbtable="demo1",
                         user='root',
                         password='MYSQL123').mode('append').save()




final = spark.read.format('jdbc').options(url='jdbc:mysql://localhost:3306/psdb',
                                driver='com.mysql.jdbc.Driver',
                                dbtable="demo1",
                                user='root',
                                password='MYSQL123').load().show()
print("sucess")