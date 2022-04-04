#URL: https://docs.opensea.io/reference/retrieving-assets-rinkeby

import requests

url = "https://testnets-api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=200"

response = requests.request("GET", url)

# See all keys in the dictionary of dictionaries
#print(assets.keys())

# Decode the JSON data into a dictionary
assets = response.json()["assets"]

#Make dictionaries of fields that we want.

#print("\nPrinting nested dictionary as a key-value pair\n")
#for i in assets:
#    if i['creator'] is not None and i['creator']['user'] is not None and i['creator']['user']['username'] is not None:
#      print("creator", i['creator']['user']['username'])
#    else:
#      print("creator", "unknown")
#    print("artwork_name", i['name'])
#    print("collection", i['collection']['name'])
#    print("nsfw", i['is_nsfw'])
#    print("currency", i['asset_contract']['symbol'])
#    print()


# Make a new list of dictionaries that we want.
transformed_assets = []

for i in assets:
    asset = {}

    if i['creator'] is not None and i['creator']['user'] is not None and i['creator']['user']['username'] is not None:
      asset['creator'] = i['creator']['user']['username']
    else:
      asset['creator'] = 'unknown'
    
    asset['artwork_name'] = i['name']
    asset['collection'] = i['collection']['name']
    asset['nsfw'] = i['is_nsfw']

    transformed_assets.append(asset)
    
# Then create a pandas dataframe out of the list.
import pandas as pd
opensea_df = pd.DataFrame(transformed_assets)
print(opensea_df)

# Save the dataframe in Parquet format.
opensea_df.to_parquet('opensea.parquet', engine='fastparquet')