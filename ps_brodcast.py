from pyspark import SparkContext
sc = SparkContext("local","ps_brodcast")
words_new = sc.broadcast(["Ashok","Chetan","Shoib","Ajay","kumar"])
data = words_new.value
print("stored data ->%s"%data)
elem = words_new.value[0]
print("Printing a particular element in RDD ->%s"%elem)