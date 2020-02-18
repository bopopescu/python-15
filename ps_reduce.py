from pyspark import SparkContext
from operator import mul,add
sc = SparkContext("local","ps_reduce")
nums = sc.parallelize([1,2,3,4,5])
multi = nums.reduce(mul)
adding = nums.reduce(add)
print("Adding all the elements -> %i"%adding)
print("Multiply all the elements ->%i"%multi)


x = sc.parallelize([("spark",1),("hadoop",4)])
y = sc.parallelize([("spark",2),("hadoop",5)])
joined = x.join(y)
col = joined.collect()
print("join RDD ->%s"%col)