sc = pyspark.SparkContext('local[*]')
# load to Spark and then to 16 dataframes of 1 million lines
spark = SparkSession(sc)