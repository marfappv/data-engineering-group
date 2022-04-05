# https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.1/hadoop-aws-3.3.1.jar
# https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.192/aws-java-sdk-s3-1.12.192.jar
# https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.192/aws-java-sdk-1.12.192.jar
# https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-core/1.12.192/aws-java-sdk-core-1.12.192.jar
# https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-dynamodb/1.12.192/aws-java-sdk-dynamodb-1.12.192.jar


#Prerequisite code
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
rdd = df.rdd

# Connecting to Postgres
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkWithPostgres')\
        .config("spark.driver.extraClassPath", "/content/postgresql-42.3.2.jar")\
        .getOrCreate()

# Enable Arrow-based columnar data transfers
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

# Create a DataFrame with Pandas-on-Spark
import pyspark.pandas as ps
ps_df = ps.DataFrame(df)
print(ps_df)

# Convert a Pandas-on-Spark Dataframe into a Pandas Dataframe
#pd_df = ps_df.select("*").toPandas()

#postgres_uri = "jdbc:postgresql://depgdb.crhso94tou3n.eu-west-2.rds.amazonaws.com:5432/marfapopova21"
#dbtable = "schema.schemata"
#user = "marfapopova21"
#password = "qwerty123"