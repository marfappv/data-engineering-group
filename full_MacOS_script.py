from helium import *
from selenium import webdriver
import pandas as pd
import requests
import time
import os
import findspark
import pyspark
from pyspark.sql import SQLContext


#Web scraping

driver = start_chrome()

def get_details(url):
    go_to(url)
    creator_name,name,collection_name,price,fav = None,None,None,None,None
    try:
      creator_name = Text(to_right_of="Created by").web_element.text
    except Exception:
      pass

    try:
      name = S('//h1[contains(@class,"title")]').web_element.text
    except Exception:
      pass
    
    try:
      collection_name = S('//div[contains(@class,"item--collection-info")]').web_element.text.split('\n')[0]
    except Exception:
      pass

    try:
      price = S('//div[contains(@class,"Price--amount")][contains(@tabindex,"-1")]').web_element.text
    except Exception:
      pass

    try:
      fav = S('//button[contains(@aria-label,"Favorited by")]').web_element.text.split("\n")[1].split(" ")[0]
    except Exception:
      pass
    
    details = {
      'creator' : creator_name,
      'artwork_name' : name,
      'collection' : collection_name,
      'price' : price,
      'favorites' : fav
    }
    return details

go_to("https://opensea.io/assets?search[sortAscending]=false&search[sortBy]=LISTING_DATE")

final_links = set()

for _ in range(5):
    links = find_all(S("//a[contains(@href,'assets/')]"))
    for i in list(map(lambda x:x.web_element.get_attribute("href"),links)):
        final_links.add(i)
    scroll_down(1000)
    time.sleep(1)

data = list(map(get_details,final_links))
opensea_ws_df = pd.DataFrame(data)
opensea_ws_df.to_parquet('opensea_ws.parquet', engine='fastparquet')

# API collection of assets from Open Sea Testnets 

def fetch_assets(page, limit, assets):
    url = "https://testnets-api.opensea.io/api/v1/assets?order_direction=desc&offset={}&limit={}".format(page*limit, limit)
    
    response = requests.request("GET", url)
    
    for a in response.json()["assets"]:
        assets.append(transform(a))

def transform(asset):
    out = {}
    out['id'] = asset['token_id']

    creator = asset['creator']
    if creator is not None and creator['user'] is not None and creator['user']['username'] is not None:
      out['creator'] = creator['user']['username']
    else:
      out['creator'] = 'unknown'
    
    out['artwork_name'] = asset['name']
    out['collection'] = asset['collection']['name']
    out['nsfw'] = asset['is_nsfw']

    return out
    
def main():
    nfts = []
    for page in range(0,20):
        fetch_assets(page, 200, nfts)
        time.sleep(1)

    opensea_API_df = pd.DataFrame(nfts)
    opensea_API_df.to_parquet('opensea_API.parquet', engine='fastparquet')

if __name__ == "__main__":
    main()

# Establishing environment and creating a dataframe from parquet file

os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home"
os.environ["SPARK_HOME"] = "/Users/Marfa-Popova/data_eng_group/spark-3.2.1-bin-hadoop3.2"
os.environ["AWS_ACCESS_KEY_ID"] = "AKIA5WZKULSM3ZZF4NHD"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

findspark.init("/Users/Marfa-Popova/data_eng_group/spark-3.2.1-bin-hadoop3.2")

sc = pyspark.SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
df = sqlContext.read.parquet("s3a://dataenggroup/parquet-data/opensea_API.parquet", header=True)

# Connecting to Postgres and imputing RDS from S3

postgres_uri = "jdbc:postgresql://nfts.cuweglfckgza.eu-west-2.rds.amazonaws.com:5432/nfts"
dbtable = "nfts.assets"
user = "marfapopova21"
password = "qwerty123"

df.write \
    .format("jdbc") \
    .mode("append") \
    .option("url", postgres_uri) \
    .option("dbtable", dbtable) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "org.postgresql.Driver") \
    .save()