from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName("List not present").getOrCreate()

list_A = [1, 2, 3, 4, 5]
list_B = [4, 5, 6, 7, 8]

df1 = spark.createDataFrame([Row(value =i) for i in list_A])
df2 = spark.createDataFrame([Row(value =i) for i in list_B])

df3 = df1.join(df2, on ="value", how = "left_anti")

df3.show()

spark.stop()

