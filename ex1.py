from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession
import pyspark

if __name__ == '__main__':
    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
    
    line = spark.read.text("C://spark-2.4.1-bin-hadoop2.7/README.md").rdd.map(lambda x: x[0])
    
    count = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x,1)).reduceByKey(add)
    
    output = count.collect()
    #output = count.sortByKey().collect() #(count.count(), key=lambda x,y:(y))
    for (word, count) in output:
        print("%s : %i " % (word, count))
        
    spark.stop()
