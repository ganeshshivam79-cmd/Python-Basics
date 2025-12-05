from pyspark.sql import SparkSession
from dotenv import load_dotenv
load_dotenv()


# Create Spark session
spark = SparkSession.builder \
    .appName("BasicExample_NoEnv") \
    .master("local[*]") \
    .getOrCreate()

# Sample data
data = [
    (101, "John", 5000),
    (102, "Jane", 6000),
    (103, "Doe", 4000),
    (104, "Mark", 7000)
]

columns = ["emp_id", "name", "salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show original DataFrame
print("Original Employee Data:")
df.show()

# Filter employees with salary > 5000
high_paid = df.filter(df.salary > 5000)

print("Employees with salary > 5000:")
high_paid.show()

# Stop Spark session
spark.stop()
