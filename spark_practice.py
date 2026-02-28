from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

spark = SparkSession.builder.appName("Spark Practice").getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("referee_id", IntegerType(), True)]
)

customer = ([1,"Will", None], [2,"Jane",None], [3,"Alex",2], [4,"Bill",None], [5,"Zack",1], [6, "Mark", 2])

df_customer = spark.createDataFrame(customer, ["id", "name","referee_id"])

df_final = df_customer.select("name").filter("referee_id != 2 or referee_id is null")

df_final.show()

spark.stop()