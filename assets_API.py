import requests
import pandas as pd

def fetch_assets(page, limit, assets):
    url = "https://testnets-api.opensea.io/api/v1/assets?order_direction=desc&offset={}&limit={}".format(page*limit, limit)
    
    response = requests.request("GET", url)
    
    for a in response.json()["assets"]:
        assets.append(transform(a))

def transform(asset):
    out = {}

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

    # Create a pandas dataframe out of the list.
    opensea_df = pd.DataFrame(nfts)
    print(opensea_df)

    # Save the dataframe in Parquet format.
    opensea_df.to_parquet('opensea.parquet', engine='fastparquet')

if __name__ == "__main__":
    main()