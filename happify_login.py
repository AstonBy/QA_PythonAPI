import requests

response1 = requests.get("https://qa06.happify.com/login/")

print(response1.cookies)

marty_session_id = response1.cookies["marty_session_id"]
marty_session_id_hash = response1.cookies["marty_session_id_hash"]
utc_offset = "120"
print(marty_session_id_hash)
print(marty_session_id)
# print(type(marty_session_id))
user_id_hash = "dbc2a6dc24e7158ace295c26aa41417a"


cookies = {
    "marty_session_id_hash": marty_session_id_hash,
    "marty_session_id": marty_session_id,
    "utc-offset": utc_offset,
    "user_id_hash": user_id_hash,
}
print(cookies)

data = {"email": "shkorkin+qa06280822@alarstudios.com", "password": "1234qwertY!"}

response2 = requests.get(
    "https://qa06.happify.com/b2b-login/", cookies=cookies, json=data
)
# user_id_hash = response2.headers.get("user_id_hash")
print(response2.cookies)
# print(user_id_hash)
print(response2.status_code)
print(response2.headers)
print(type(response2.headers))


print(type(response2))

response3 = requests.get("https://qa06.happify.com/", cookies=cookies)

print(response3.status_code)
print(response3.cookies)
print(response3.headers)

headers = response3.headers.get("X-XSS-Protection")
print(headers)

remember_token = "1030|2a29889872e4d1dd8685e64d94741dc397ab47cb"
cookies1 = {
    "marty_session_id_hash": marty_session_id_hash,
    "marty_session_id": marty_session_id,
    "utc-offset": utc_offset,
    "user_id_hash": user_id_hash,
}
response4 = requests.get(
    "https://qa06.happify.com/api/homepage/",
    cookies=cookies1,
    headers={
        "X-XSS-Protection": headers,
        "remember_token": remember_token,
        "user_id_hash": user_id_hash,
    },
)

print(response4.status_code)
print(response4.cookies)
