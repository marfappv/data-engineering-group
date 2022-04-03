#URL: https://docs.opensea.io/reference/retrieving-collections-testnets

import requests

url = "https://testnets-api.opensea.io/api/v1/collections?offset=0&limit=300"

response_collections = requests.request("GET", url)

print(response_collections.text)

# if want to print the output in shell, write 'python3 data_eng_group/collections_via_API.py'
# if you want to see the outpu in a separate window, write 'python3 data_eng_group/collections_via_API.py >> output'
