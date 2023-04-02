import requests

payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response1.text)
print(dict(response1.cookies))

cookie_value = response1.cookies.get('auth_cookie')

print(cookie_value)

cookies = {}
print(cookies)

if cookie_value is not None:
         cookies.update({'auth_cookie': cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)


print(response2.text)
#print(response.status_code)
#print(dict(response.cookies))


#print(response.headers)