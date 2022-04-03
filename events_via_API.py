#URL: https://docs.opensea.io/reference/retrieving-events-testnets

import requests

url = "https://testnets-api.opensea.io/api/v1/events?only_opensea=false&offset=0&limit=20"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "5bec8ae0372044cab1bef0d866c98618"
}

response_events = requests.request("GET", url, headers=headers)

print(response_events.text)

# if want to print the output in shell, write 'python3 data_eng_group/events_via_API.py'
# if you want to see the outpu in a separate window, write 'python3 data_eng_group/events_via_API.py >> output'