from pyspark.sql import SparkSession
import argparse
from pyspark.sql.functions import col, from_unixtime, to_timestamp, avg, sum as _sum, date_format
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, LongType, DoubleType
parser = argparse.ArgumentParser()
parser.add_argument('--date', required=True, help='DD-MM-YYYY')
args = parser.parse_args()
proc_date = args.date.replace('-', '')
spark = ( SparkSession.builder 
         .appName('vodafone-network-pipeline') 
         .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') 
         .config('spark.sql.catalog.mycat','org.apache.iceberg.spark.SparkCatalog')
         .config('spark.sql.catalog.mycat.warehouse','s3://vodafone-warehouse/')
         .getOrCreate())
schema = StructType([ StructField('tower_id', IntegerType(), False),
                     StructField('region', StringType(), False), 
                     StructField('timestamp', LongType(), False), 
                     StructField('signal_strength', DoubleType(), False),
                     StructField('data_volume_mb', DoubleType(), False) ])
raw_path = f"s3://raw-telecom-network-data/network_metrics_{proc_date}.csv"
bronze_path = f"s3://telecom-bronze/network_metrics/date={args.date}/"

/*Bronze Layer*/
