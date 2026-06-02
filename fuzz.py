# I wrote this script in order to not guess all the possible paths that lead to deleting the messages

import requests
import warnings
warnings.filterwarnings('ignore')  # silence the SSL warnings

words = ['delete', 'messages', 'message', 'all', 'drop', 'admin', 'clear', 'remove']

paths = []
for w1 in words:
    paths.append(f'/{w1}')
    for w2 in words:
        if w1 != w2:
            # try with slash: /delete/messages maybe?
            paths.append(f'/{w1}/{w2}')
            # try with underscore: /delete_messages perhaps?
            paths.append(f'/{w1}_{w2}')
            for w3 in words:
                if w3 != w1 and w3 != w2:
                    # try 3 words with underscores: /delete_all_messages perchance?
                    paths.append(f'/{w1}_{w2}_{w3}')

for path in paths:
    url = f'https://localhost:5000{path}'
    try:
        response = requests.get(url, verify=False)
        if response.status_code != 404:
            print(f'FOUND: {url} - status: {response.status_code}')
    except:
        pass  # ignore errors

print("Done!")