from pyspark import SparkContext
sc = SparkContext("local","ps_accumulator")
num = sc.accumulator(1)
def f(x):
    global num
    num+=x
rdd = sc.parallelize([2,3,4,5])
rdd.foreach(f)
final = num.value
print("Accumulated value is -> %i"%final)