import requests
import json

Client_Id =	'ec34c6f7de41a54a258a'
Client_Secret =	'1ca6e727b5d3eacfa17af22253b78b6e'

response = requests.post('https://api.artsy.net/api/tokens/xapp_token', data={
                                                                            'client_id':Client_Id,
                                                                            'client_secret':Client_Secret
                                                                            })
# print(response.status_code)
# print(response.text)
# print(response.headers)
# print(json.loads(response.text)["token"])
token = json.loads(response.text)["token"]
#artist_id = input()
headers = {"X-XAPP-Token": token}
# response1 = requests.get(f'https://api.artsy.net/api/artists/{artist_id}', headers=headers)
#
# print(json.loads(response1.text)['birthday'])
spis = []
with open(input("FileName: ")) as f:
    for art in f:
        response1 = requests.get(f'https://api.artsy.net/api/artists/{art.rstrip()}', headers=headers)
        #print(f'https://api.artsy.net/api/artists/{art}')
        artist_data = f'{json.loads(response1.text)["birthday"]}-{json.loads(response1.text)["name"]}'
        spis += list(artist_data)
    print(list(spis))

# dataset_24476_4(4).txt