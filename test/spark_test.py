import sys
sys.path.append("E:\\项目代码\\python_workspace\\SPARKSQL_ON_HIVE")
import numpy as np
import pandas as pd
import findspark
findspark.init()
import pyspark
from utils.spark_utils import start_or_get_spark

print("Spark version:{}".format(pyspark.__version__))

config={"spark.cores.max":3,'spark.debug.maxToStringFields':'50'}
spark=start_or_get_spark("ALS",config=config)
sc=spark.sparkContext
# 输入数据
data = ["hello", "world", "hello", "world"]

# 将collection的data转为spark中的rdd并进行操作
rdd = sc.parallelize(data)
res_rdd = rdd.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# 将rdd转为collection并打印
res_rdd_coll = res_rdd.collect()
for line in res_rdd_coll:
    print(line)
sc.stop()
print('计算成功！')

