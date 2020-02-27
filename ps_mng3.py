from pyspark.shell import sqlContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("name_app")\
    .config("spark.mongodb.input.uri","mongodb://192.168.1.96:27017/mydatabase.data")\
    .config("spark.mongodb.output.uri","mongodb://192.168.1.96:27017/mydatabase.data").getOrCreate()
data = spark.createDataFrame([("Bilbo Baggins",  50), ("Gandalf", 1000), ("Thorin", 195), ("Balin", 178), ("Kili", 77),
   ("Dwalin", 169), ("Oin", 167), ("Gloin", 158), ("Fili", 82), ("Bombur", None)], ["name", "age"])
#data.write.format("com.mongodb.spark.sql.DefaultSource").option("database","mydatabase").option("collection","data").save()
data.show()
data.registerTempTable("mytable")
res = sqlContext.sql("select * from mytable limit 5")
res.show()