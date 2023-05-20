#!/usr/bin/env python

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    from_json, col, format_number
)
from pyspark.sql.types import (
    StringType, FloatType, StructType, StructField
)


def main():
    spark = SparkSession \
        .builder \
        .appName('LocalStreamSample') \
        .getOrCreate()

    # Create DataFrame for input Stream
    data = spark \
        .readStream \
        .format('socket') \
        .option('host', 'localhost') \
        .option('port', '9999') \
        .load()

    schema = StructType(
        [
            StructField('account_id', StringType(), True),
            StructField('account_region', StringType(), True),
            StructField('transaction_value', FloatType(), True),
        ]
    )

    # Stream Listening View
    json_data = data.withColumn(
                'json_data', 
                from_json(col('value'), schema)
            ) \
            .select('json_data.*')

    # Credit Flow by Region View
    region_data = json_data.groupBy('account_region').sum() \
            .withColumn(
                'credit_flow', 
                format_number('sum(transaction_value)', 2)
            ) \
            .select(['account_region', 'credit_flow'])

    query = region_data \
        .writeStream \
        .outputMode("complete") \
        .format('console') \
        .start()

    query.awaitTermination()

if __name__ == '__main__':
    main()
