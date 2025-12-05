from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import *


df.withColumnRenamed("data1","data")                    "-- rename a column"
df.cache()
df = df.withColumn("calldate",to_char("calldate","MM/dd/yyyy"))
.withColumn("AvailableTime",to_timestamp("Available_time","MM/dd/yyyy hh:mm:ss a"))
.withColumn("Delay",round("Delay",2))

display(df) -- dislay output

df.printSchema() -- "shows all column and dt types -- utility"

#############################################################################################

spark = SparkSession.builder.appName("ReadCSVWithOptions").getOrCreate()

# Read CSV using .option()
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("path/to/your/file.csv")

--- Another way

df = spark.read \
    .format("csv") \
    .option("header", "true") \        # Use first row as header
    .option("inferSchema", "true") \   # Automatically infer data types
    .load("data/fights.csv")

inferschema is for datatype aligning but it wont work 100 percent

.load("data/fights*.csv") --- wildcard multiple files can be read

""" for json """
df = spark.read \
    .format("json") \
    .option("multiLine", "true") \         # Optional: only if each JSON spans multiple lines
    .load("data/fights*.json")

""" for parquet """
df = spark.read \
    .format("parquet") \
    .option("multiLine", "true") \
    .load("data/fights*.parquet")



from pyspark.sql.types import StructType, StructField, StringType, IntegerType
schema = StructType([StructField("name", StringType(), True),
                     StructField("age", IntegerType(), True)])
df = spark.read.format("csv").option("header", "true").schema(schema).load("path/to/file.csv")
df.schema.simpleString()


schema = "id INT, name STRING, age INT, salary DOUBLE"
df = spark.read.option("header", "true").schema(schema).csv("path/to/file.csv")
df.schema.simpleString()

schema = "id INT, name STRING, age INT, salary DOUBLE"
df = spark.read.format("csv").option("header", "true").schema(schema).load("path/to/file.csv")