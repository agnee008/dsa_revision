from pyspark.sql import SparkSession, Row
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, monotonically_increasing_id
spark = SparkSession.builder.appName("Index").getOrCreate()

# data = [Row(event_id =i) for i in [1, 2, 3, 4, 5, 6]]

# df = spark.createDataFrame(data)

# df.show()

data = [("John", 25), ("Jane", 35), ("Jake", 28)]

df = spark.createDataFrame(data, ["name", "age"])

w = Window.orderBy(monotonically_increasing_id())
df = df.withColumn("index", row_number().over(w) -1)

df.show()

spark.stop()
