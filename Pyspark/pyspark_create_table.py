from pyspark.sql import SparkSession
from pyspark.sql import Row

# 1. Enable Spark Session with Hive support
spark = SparkSession.builder \
    .appName("SparkTableWrites") \
    .enableHiveSupport() \
    .getOrCreate()

# Sample DataFrame
data = [
    Row(customer_id=1, name="Alice", region="US", year=2023, order_date="2023-01-15"),
    Row(customer_id=2, name="Bob", region="IN", year=2024, order_date="2024-03-10"),
    Row(customer_id=3, name="Charlie", region="US", year=2023, order_date="2023-05-20")
]
df = spark.createDataFrame(data)

# --- 1. Write to default table ---
df.write.mode("overwrite").saveAsTable("my_default_table")

# --- 2. Write to a table in a different schema (database) ---
# Make sure database `analytics` exists
spark.sql("CREATE DATABASE IF NOT EXISTS analytics")
df.write.mode("overwrite").saveAsTable("analytics.sales_table")

# --- 3. Write using bucketBy and sortBy ---
# Note: saveAsTable + bucketBy requires Hive support
df.write \
  .bucketBy(4, "customer_id") \
  .sortBy("order_date") \
  .mode("overwrite") \
  .saveAsTable("bucketed_sales_table")

"""
4 bucket files will be created under tablename
"""

# --- 4. Write using partitionBy ---
df.write \
  .mode("overwrite") \
  .partitionBy("region", "year") \
  .saveAsTable("partitioned_sales_table")

"""
/user/hive/warehouse/partitioned_sales_table/
├── region=US/year=2023/
│   └── part-00000-*.parquet
├── region=IN/year=2024/
│   └── part-00001-*.parquet
"""
