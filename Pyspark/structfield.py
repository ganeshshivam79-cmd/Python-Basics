from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DateType
from pyspark.sql.functions import to_date

# Step 1: Spark Session
spark = SparkSession.builder.appName("JSONWithSchema").getOrCreate()

# Step 2: Define StructType schema (optional)
custom_schema = StructType([
    StructField("id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("event_date", StringType(), True)  # Parse this later
])

# Step 3: Read JSON with StructType schema
df = spark.read \
    .schema(custom_schema) \
    .option("multiLine", "true") \
    .json("data/sample.json")

# Step 4: Convert date and filter
df_filtered = df.withColumn("event_date_parsed", to_date("event_date", "M/d/y")) \
                .filter("event_date_parsed >= '2023-01-01'")

df_filtered.show()

# Step 5: Read JSON with DDL schema string directly
ddl_schema = "`id` STRING, `name` STRING, `event_date` STRING"

df2 = spark.read \
    .schema(ddl_schema) \
    .option("multiLine", "true") \
    .json("data/sample.json")

df2.show()


"Use struct field or ddl for column properties"