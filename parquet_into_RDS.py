# https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.1/hadoop-aws-3.3.1.jar
# https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.192/aws-java-sdk-s3-1.12.192.jar
# https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.192/aws-java-sdk-1.12.192.jar
# https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-core/1.12.192/aws-java-sdk-core-1.12.192.jar
# https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-dynamodb/1.12.192/aws-java-sdk-dynamodb-1.12.192.jar

import os
os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home"
os.environ["SPARK_HOME"] = "/Users/Marfa-Popova/data_eng_group/spark-3.2.1-bin-hadoop3.2"
os.environ["AWS_ACCESS_KEY_ID"] = "AKIA5WZKULSM3ZZF4NHD"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

import findspark
findspark.init("/Users/Marfa-Popova/data_eng_group/spark-3.2.1-bin-hadoop3.2")
import pyspark
from pyspark.sql import SQLContext

sc = pyspark.SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
df = sqlContext.read.parquet("s3a://dataenggroup/parquet-data/opensea_API.parquet", header=True)

# Connecting to Postgres
#psql --host=nfts.cuweglfckgza.eu-west-2.rds.amazonaws.com --port=5432 --username=marfapopova21 --password --dbname=nfts
postgres_uri = "jdbc:postgresql://nfts.cuweglfckgza.eu-west-2.rds.amazonaws.com:5432/nfts"
dbtable = "nfts.assets"
user = "marfapopova21"
password = "qwerty123"

df.write \
    .format("jdbc") \
    .mode("overwrite") \
    .option("url", postgres_uri) \
    .option("dbtable", dbtable) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "org.postgresql.Driver") \
    .save()
