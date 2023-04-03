import requests

response1 = requests.get("https://qa06.happify.com/login/")

print(response1.cookies)

marty_session_id = response1.cookies["marty_session_id"]
marty_session_id_hash = response1.cookies["marty_session_id_hash"]


cookies = {"marty_session_id_hash": marty_session_id_hash,
           "marty_session_id": marty_session_id}


data = {"email":"shkorkin+qa06280822@alarstudios.com","password":"1234qwertY!"}

response2 = requests.post("https://qa06.happify.com/b2b-login/",
                         json=data,
                         cookies=cookies
                         )

print(response2.cookies)
print(response2.status_code)
print(response2.headers)
print(response2.text)


# response3 = requests.get("https://qa06.happify.com/", cookies=cookies)
#
# print(response3.status_code)
# print(response3.cookies)
# print(response3.headers)

# headers = response3.headers.get("X-XSS-Protection")
# print(headers)

# remember_token= "1030|2a29889872e4d1dd8685e64d94741dc397ab47cb"
# cookies1 = {"marty_session_id_hash": marty_session_id_hash,
#            "marty_session_id": marty_session_id,
#            "utc-offset": utc_offset,
#            "user_id_hash": user_id_hash}
response4 = requests.get("https://qa06.happify.com/api/homepage/",
                         cookies= cookies
                         # headers= {
                         #     "X-XSS-Protection": headers,
                         #     "remember_token": remember_token,
                         #     "user_id_hash": user_id_hash
                         #        }
                         )

print(response4.status_code)
print(response4.cookies)
result = response4.json()
print(result)
print(result['track']['name'])

response5 = requests.get("https://qa06.happify.com/environment/",
                        cookies=cookies
                        )

print(response5.status_code)
print(response5.text)
print(response5.json()['available_locales']['b2b'])
print(response5.json()['git_hash'])
