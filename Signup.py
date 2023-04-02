import requests

response = requests.get("https://qa06.happify.com/")

print(dict(response.cookies))
print(response.status_code)

cookie_value1 = response.cookies.get("marty_session_id")
cookie_value2 = response.cookies.get("marty_session_id_hash")

cookies_reg = {
    "marty_session_id": cookie_value1,
    "marty_session_id_hash": cookie_value2,
}

print(cookies_reg)

response2 = requests.post("https://qa06.happify.com/pre-signup/")

print(response2.text)
print(dict(response2.cookies))

username = "username"
email = "email"
password = "password"
agreement = "agreement"

data = {
    username: "AST",
    email: "shkorkin+qa06220822_9@alarstudios.com",
    password: "1234qwertY!",
    agreement: "on",
}

response1 = requests.post(
    "https://qa06.happify.com/email-register/", data=data, cookies=cookies_reg
)

print(response1.status_code)
print(response1.text)
