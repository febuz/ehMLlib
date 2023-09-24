# set pyspark
import py4j
from multiprocessing import Pool
import operator
########################################################
######## IMPORTING NECESSARY MODULES AND MODELS ########
########################################################
import pyspark
from pyspark import SparkConf, SparkContext, SparkFiles
from pyspark.sql.functions import pandas_udf, udf, PandasUDFType
from pyspark.sql.types import DoubleType, StructField
from pyspark.sql.functions import udf, collect_list
from pyspark.sql.window import Window
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
from pyspark.sql.functions import to_date
from pyspark.sql.functions import date_format
from pyspark.sql.functions import unix_timestamp
from pyspark.sql.functions import from_unixtime
#pyspark sql and pyspark mllib
from pyspark.sql import SparkSession,SQLContext as sqlContext
from pyspark.sql import HiveContext
from pyspark.sql.functions import col, trim, to_date, min, max
from pyspark.sql.types import *
from pyspark.sql import functions as F 
from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import col, lit
from pyspark.ml.feature import StringIndexer, VectorAssembler,VectorIndexer
from pyspark.ml import Pipeline
from pyspark.ml.regression import GBTRegressor
from pyspark.ml.feature import Binarizer
from pyspark.conf import SparkConf
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator,MulticlassClassificationEvaluator, BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
import findspark
import pyspark
sc = pyspark.SparkContext('local[*]')
# load to Spark and then to 16 dataframes of 1 million lines
spark = SparkSession(sc)
