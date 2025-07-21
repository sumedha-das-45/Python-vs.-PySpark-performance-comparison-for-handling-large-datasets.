from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
import time

spark = SparkSession.builder.appName("PySparkVsPandas").getOrCreate()
start = time.time()

df = spark.read.csv("large_dataset.csv", header=True, inferSchema=True)
filtered = df.filter(col("age") > 30)
agg = filtered.groupBy("department").agg(avg("salary").alias("avg_salary"))

print("PySpark Result:")
agg.show()

print(f"PySpark processing time: {time.time() - start:.2f} seconds")
