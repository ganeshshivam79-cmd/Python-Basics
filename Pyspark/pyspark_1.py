from pyspark.sql import SparkSession
from dotenv import load_dotenv
load_dotenv()

# Create Spark session
spark = SparkSession.builder \
    .appName("BasicExample") \
    .getOrCreate()

# Create a DataFrame from a list of tuples
data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
columns = ["id", "name"]

df = spark.createDataFrame(data, columns)

# Show the DataFrame
print("Original DataFrame:")
df.show()

# Filter rows where id > 1
filtered_df = df.filter(df.id > 1)

print("Filtered DataFrame (id > 1):")
filtered_df.show()

# Stop the Spark session
spark.stop()
