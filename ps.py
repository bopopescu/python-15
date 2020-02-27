"""SimpleApp1.py"""
from pyspark import SparkContext as sc

logFile = "/home/tibil/Downloads/spark-2.4.4-bin-hadoop2.7/README.md"  # Should be some file on your system
sc = sc("local", "ps")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))