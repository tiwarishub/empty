import requests
import os

ACTIONS_RUNTIME_TOKEN = os.environ.get("ACTIONS_RUNTIME_TOKEN")
CACHE_URL = os.environ.get("CACHE_URL")
print("cache url",CACHE_URL)

response = requests.get(url = CACHE_URL, headers = {"Authorization": "Bearer " + ACTIONS_RUNTIME_TOKEN})

print(response.json())

archiveLocation = response.json()["archiveLocation"]
print("Archive location", archiveLocation)

blobStoreResponse = requests.get(url = archiveLocation)

print(blobStoreResponse.headers, blobStoreResponse.status_code)


