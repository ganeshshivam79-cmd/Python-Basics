from newcode import path_log

df.repartition(4) \
  .write \
  .option("header", "true") \
  .option("maxRecordsPerFile", 10000) \
  .csv("path/to/output_with_repartition/")
🔁 This just splits output into ~4 files with max 10,000 records each (no folder structure).

df.write \
    .option("header", "true") \
    .option("maxRecordsPerFile", 10000) \
    .partitionBy("country", "year") \
    .csv("path/to/output_with_partitionby/")

"""This  creates folder structure like / country = US / year = 2024 /
No control on number of files — depends on data distribution."""

so we can write the file based on our need


spark.write will create output path

mode("ignore") → silently skips writing
mode("error") → throws an error
mode("overwrite") → deletes and rewrites
mode("append") → adds new data to existing file