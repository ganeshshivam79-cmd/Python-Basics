# pyspark_basics_keywords.py

import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Set environment variables if needed (optional)
os.environ["JAVA_HOME"] = r"F:\lib_function\jdk-11"
os.environ["HADOOP_HOME"] = r"F:\lib_function\hadoop"
os.environ["SPARK_HOME"] = r"F:\lib_function\spark-3.5.6-bin-hadoop3"

# Create SparkSession
spark = SparkSession.builder \
    .appName("PySpark Basics") \
    .getOrCreate()

# Sample data
data = [("Alice", 24), ("Bob", 30), ("Charlie", 28)]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

print("📋 Original DataFrame:")
df.show()

# Filter
df_filtered = df.filter(col("Age") > 25)
print("🔍 Filtered (Age > 25):")
df_filtered.show()


# Add column
df_new = df.withColumn("DoubleAge", col("Age") * 2)
print("➕ New Column (DoubleAge):")
df_new.show()

# GroupBy and count
print("📊 Group by Age:")
df.groupBy("Age").count().show()

# Stop session
spark.stop()
