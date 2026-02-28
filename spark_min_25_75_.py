from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import max, lit

spark = SparkSession.builder.appName("Stats").getOrCreate()

data = [("A", 10), ("B", 20), ("C", 30), ("D", 40), ("E", 50), ("F", 15), ("G", 28), ("H", 54), ("I", 41), ("J", 86)]

df = spark.createDataFrame(data, ["Name", "Score"])

max_score = df.select(max("Score")).collect()[0][0]

df_max = df.withColumn("max_score", lit(max_score))

df_max.show()
spark.stop()

