from pyspark import SparkContext
sc=SparkContext("local","ps1")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"]
)
counts = words.count()
collect=sorted(words.collect())
print("number of elements in RDD -> %i"%counts)
print("elements in RDD -> %s"%collect)
def f(x):print(x)
fore = words.foreach(f)

words_filter = words.filter(lambda  x:"spark" in x)
filtered = words_filter.collect()
print("Filtered RDD -> %s"%filtered)

words_map = words.map(lambda x:(x,1))
mapping = words_map.collect()
print("key value pair -.%s"%mapping)

words.cache()
caching = words.persist().is_cached
print("words got cached->%s"%caching)