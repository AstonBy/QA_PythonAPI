import re
import requests

response = requests.get("https://qa02.happify.com/admin/login/")

token = re.findall('id="csrf_token".*value="(.*?)"', response.text)[0]

marty_session_id = response.cookies["marty_session_id"]
marty_session_id_hash = response.cookies["marty_session_id_hash"]

data = {
    "access_token": "",
    "csrf_token": token,
    "email": "shkorkin@alarstudios.com",
    "password": "12341234",
    "agree_rules": "y"}
response1 = requests.post("https://qa02.happify.com/admin/login/",
                          data=data,
                          cookies={
                              "marty_session_id": marty_session_id,
                              "marty_session_id_hash": marty_session_id_hash
                          })

admin_token = response1.cookies["admin_token"]
response2 = requests.get("https://qa02.happify.com/admin/connect-spaces/edit/?id=9&url=%2Fadmin%2Fconnect-spaces%2F",
                         cookies={
                             "admin_token": admin_token,
                             "marty_session_id": marty_session_id,
                             "marty_session_id_hash": marty_session_id_hash
                          })

domain = re.findall('id="design_set".*selected value="(.*?)"', response2.text)
print(domain)

response3 = requests.get("https://qa02.happify.com/admin/modality-packages/edit/?id=1&url=%2Fadmin%2Fmodality-packages%2F",
                         cookies={
                             "admin_token": admin_token,
                             "marty_session_id": marty_session_id,
                             "marty_session_id_hash": marty_session_id_hash
                          })

h = 0
j = []
modality = re.findall(f'id="modalities-{h}-modality".*selected value="(.*?)"', response3.text)
while modality != []:
    j += modality
    h += 1
    modality = re.findall(f'id="modalities-{h}-modality".*selected value="(.*?)"', response3.text)
else:
    print(j)



