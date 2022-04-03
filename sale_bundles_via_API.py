#URL = https://docs.opensea.io/reference/retrieving-bundles-testnet

import requests

url = "https://testnets-api.opensea.io/api/v1/bundles?limit=20&offset=0"

response_sale = requests.request("GET", url)

print(response_sale.text)

# if want to print the output in shell, write 'python3 data_eng_group/sale_bundles_via_API.py'
# if you want to see the outpu in a separate window, write 'python3 data_eng_group/sale_bundles_via_API.py >> output'
