from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import count, col, when

spark = SparkSession.builder.appName("Stats").getOrCreate()

data = [
Row(name='John', job='Engineer'),
Row(name='John', job='Engineer'),
Row(name='Mary', job='Scientist'),
Row(name='Bob', job='Engineer'),
Row(name='Bob', job='Engineer'),
Row(name='Bob', job='Scientist'),
Row(name='Sam', job='Doctor'),
]

df = spark.createDataFrame(data, ["name", "job"])

count_df = df.groupBy("job").agg(count("job").alias("count"))

top_jobs = count_df.orderBy(col("count").desc()).limit(2)
top_jobs_list = [Row["job"] for Row in top_jobs.collect()]

df_transformed = df.withColumn("job", when(col("job").isin(top_jobs_list), col("job")).otherwise("Other"))
# Show results
df_transformed.show()

# Stop SparkSession
spark.stop()
