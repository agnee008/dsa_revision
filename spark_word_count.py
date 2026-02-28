from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# Initialize SparkSession
spark = SparkSession.builder.appName("Word Count").getOrCreate()

# Read the text file
test_file = spark.read.text("test_file.txt")

# Split lines into words, explode to separate rows, and count occurrences
word_count_df = test_file.select(explode(split(col("value") , " ")).alias("word")).groupBy("word").count()
# Show the result
word_count_df.show()

# Stop the SparkSession
spark.stop()





