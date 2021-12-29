from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName('spark')
sc = SparkContext(conf = conf)

