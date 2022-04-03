#URL: https://docs.opensea.io/reference/retrieving-assets-rinkeby

import requests

url = "https://testnets-api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20"

response_assets = requests.request("GET", url)

print(response_assets.text)

# if want to print the output in shell, write 'python3 data_eng_group/assets_via_API.py'
# if you want to see the outpu in a separate window, write 'python3 data_eng_group/assets_via_API.py >> output'