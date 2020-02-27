from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spar_mon")\
    .config("spark.mongodb.input.uri","mongodb://192.168.1.96:27017/test.ask1")\
    .config("spark.mongodb.output.uri","mongodb://192.168.1.96:27017/test.ask1").getOrCreate()

abc = spark.read.csv("/home/tibil/Downloads/Fire_Incidents_Data.csv",header=True)
abc.write.format("com.mongodb.spark.sql.DefaultSource").option("database","test").option("collection","ask1").save()
