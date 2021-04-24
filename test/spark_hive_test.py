import os
from os.path import join, abspath

import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import Row

###
# 1)运行之前需要设置warehouse系统权限：D:\hadoop-3.2.1\winutils\hadoop-3.2.1\bin\winutils.exe chmod 777 e:\data\hive\hive-data\tmp
# 2)解析json表时，需要将对hive/lib中对应的hive-hcatalog-core-3.1.2.jar复制到spark/jars
# ###

#os.environ["HADOOP_USER_NAME"] = "root"

warehouse_location = abspath('spark-warehouse')
#print(warehouse_location)
# warehouse_location points to the default location for managed databases and tables
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("select count(1) from cct_dev.dwd_event_log").show()