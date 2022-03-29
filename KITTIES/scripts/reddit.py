
import requests

auth = requests.auth.HTTPBasicAuth('T1almc7dHjX0znpPqI-VOg', 'BVlCZiQTaqXyK7IU0SW3WEnRjt8i-A')

data = {'grant_type': 'password',
        'username': 'Little_RR',
        'password': '090308grantchen888'}

headers = {'User-Agent': 'MyApi/0.0.1 '}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)


res = requests.get("https://www.reddit.com/user/ickybus/m/generalcats/",
                   headers=headers)

print(res.json())