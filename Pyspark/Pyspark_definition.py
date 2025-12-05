from multiprocessing.pool import job_counter

Transformation
"Tranform one dataframe to another"
Narrow vs wide
"Transformation performed on single par"


read, write, collect, show
("all are actions ")  use collect instead of show

SparkUI will go live only on execution
"localhost:4040"

spark will make jobs, stages and tasks. tasks will taken by executor to do the job

Spark SQL Engine is a powerful compiler that optimizes your code and also generates efficient
ByteJava code

"SparkSQL"
df.createOrReplaceTempView("survey_tab")
a1=spark.sql("select")
a1.show()

The Spark SQL Engine is the core execution engine behind:

✅ spark.sql() (SQL queries)
✅ DataFrame API
✅ Dataset API

"""See SparkSQL engine txt documentation"""



converting csv to spark dataframe , now the data will be stored in different nodes where each node 
have many partition and , we can create code to filter out our condition will go to driver and then 
executor right

Parquet files always come with schema information embedded in the file itself. This is one of the key
advantages of using the Parquet format. so use parquet files mostly

"DataFrameReader API will be different for each file to read data"

Lazy evaluation in Spark means Spark does not execute operations immediately when you define them
(like .select(), .filter(), .withColumn(), etc.). Instead, it builds a logical plan (a DAG) and
waits until an action (like .show(), .collect(), .write()) is called to actually run the computation.

Use Structfield and schema for giving proper datatype to a column

