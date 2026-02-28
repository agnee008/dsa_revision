from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Combine List").getOrCreate()

# Lists
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]

# Combine lists into a list of tuples
data = list(zip(list1, list2))

# Create DataFrame directly from the list of tuples
df = spark.createDataFrame(data, ["column1", "column2"])

# Show the DataFrame
df.show()

# Stop SparkSession
spark.stop()
