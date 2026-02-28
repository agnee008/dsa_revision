from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import min, max

# Initialize SparkSession
spark = SparkSession.builder.appName("FindMissingValues").getOrCreate()

# Sample data
data = [1, 2, 3, 5, 7]

# Create DataFrame from the list
df = spark.createDataFrame([Row(value=i) for i in data])

# Get the minimum and maximum values using select
min_value = df.select(min("value")).collect()[0][0]
max_value = df.select(max("value")).collect()[0][0]

# Create a DataFrame representing the full range of numbers
full_range_df = spark.range(min_value, max_value + 1).toDF("value")

# Perform a left anti join to find missing values
missing_values_df = full_range_df.join(df, "value", "left_anti")

# Show the missing values
missing_values_df.show()

# Stop SparkSession
spark.stop()


