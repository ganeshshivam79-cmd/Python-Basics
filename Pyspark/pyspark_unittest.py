import unittest
from pyspark.sql import SparkSession
from pyspark.sql import Row

class PySparkGroupByTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .appName("PySparkUnitTest") \
            .master("local[*]") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_groupby_sum(self):
        data = [
            Row(department="Sales", salary=5000),
            Row(department="Sales", salary=4000),
            Row(department="HR", salary=3000)
        ]
        df = self.spark.createDataFrame(data)

        # Actual result
        result_df = df.groupBy("department").sum("salary") \
            .withColumnRenamed("sum(salary)", "total_salary")

        # Expected result
        expected_data = [
            Row(department="HR", total_salary=3000),
            Row(department="Sales", total_salary=9000)
        ]
        expected_df = self.spark.createDataFrame(expected_data)

        self.assertEqual(
            sorted(result_df.collect()),
            sorted(expected_df.collect())
        )
if __name__ == "__main__":
    unittest.main()