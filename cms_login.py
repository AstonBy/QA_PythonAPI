# import requests
#
# class TestCmsLogin:
#     def test_cms_login(self):
#         data = {'email': 'shkorkin@alarstudios.com', 'password': '1234qwertY!'}
#
#         response = requests.get("https://qa06.happify.com/admin/login/?next=%2Fadmin%2F%3F", json=data)
#         assert "marty_session_id" in response.cookies, "нету MSI"
#         assert "marty_session_id_hash" in response.cookies, "нету MSIH"
#         assert "x-csrf-token" in response.headers, "нету CSRF"

import requests

response1 = requests.get("https://qa06.happify.com/admin/")
marty_session_id = response1.cookies["marty_session_id"]
marty_session_id_hash = response1.cookies["marty_session_id_hash"]

print(marty_session_id_hash)
print(marty_session_id)
print(response1.text)





# data = {
#     "email": "shkorkin@alarstudios.com",
#     "password": "1234qwertY!", "agree_rules": "y"
#        }

# cookies = {'marty_session_id_hash': marty_session_id_hash,
#            'marty_session_id': marty_session_id,
#            'X-XSS-Protection': '1; mode=block'}
#
# response = requests.post("https://qa06.happify.com/admin/login/", json=data, cookies=cookies, allow_redirects=True)
#
# print(response.status_code)
# print(response.headers)
# print(response.cookies)
# print(response.text)
