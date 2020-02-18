from pyspark import SparkContext,SparkConf
from  pyspark import BasicProfiler
class Mycustomprofiler(BasicProfiler):
    def show(self, id):
        print("my custom profiles for RDD:%s"%id)

    """ def show(self, id):
               stats = self.stats()
               if stats:
                   print("=" * 60)
                   print("Profile of RDD<id=%d>" % id)
                   print("=" * 60)
                   stats.sort_stats("time", "cumulative").print_stats()"""

conf = SparkConf().set("spark.python.profile","true")
sc = SparkContext('local','ps_profile', conf=conf, profiler_cls=Mycustomprofiler)
print(sc.parallelize(range(1000)).map(lambda x: 2 * x).take(10))
print(sc.parallelize(range(10)).count())
print(sc.parallelize(range(1000)).map(lambda x: 3 * x).take(10))
print(sc.parallelize(range(1000)).count())
sc.show_profiles()


