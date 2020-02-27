from pyspark.shell import sqlContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ps_mng2")\
    .config("spark.mongodb.input.uri","mongodb://192.168.1.96:27017/mydatabase.rest")\
    .config("spark.mongodb.output.uri","mongodb://192.168.1.96:27017/mydatabase.rest").getOrCreate()

people = spark.read.json("/home/tibil/Downloads/restaurants.json")
#people.write.format("com.mongodb.spark.sql.DefaultSource").option("database","mydatabase").option("collection","rest").mode("append").save()


df = spark.read.format("com.mongodb.spark.sql.DefaultSource")\
    .option("uri","mongodb://192.168.1.96:27017/mydatabase.rest").load()
df.registerTempTable("mycol")
res = sqlContext.sql("select * from mycol where 'borough'='Bronx'")
res.show()