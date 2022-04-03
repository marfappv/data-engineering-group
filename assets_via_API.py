#URL: https://docs.opensea.io/reference/retrieving-assets-rinkeby

import requests

url = "https://testnets-api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20"

response = requests.request("GET", url)

# if want to print the output in shell, write 'python3 data_eng_group/assets_via_API.py'
# if you want to see the outpu in a separate window, write 'python3 data_eng_group/assets_via_API.py > output'

# Decode the JSON data into a dictionary
assets = response.json()["assets"]

# Need to make a new list of dictionaries that we want.
# Then we'll create a pandas dataframe out of it and save in Parquet format.

# Print each key-value pair in
collection = []

for a in assets:
    x = a['collection']
    collection.append(x)
    #print(a)
    #print("\n\n")