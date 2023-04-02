import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserGet(BaseCase):
    def test_user_no_auth(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_name(response, "username", 2, "ERROR")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_user_details_with_creds(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = requests.post(
            "https://playground.learnqa.ru/api/user/login",
            data=data
        )
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value()

        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}")
