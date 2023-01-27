import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserGet(BaseCase):
    def test_user_no_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_name(response, "username", "Vitaliy", "There is no username or another one")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_user_details_with_creds(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = MyRequests.post(
            "/user/login",
            data=data
        )

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")


        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                 cookies={"auth_sid": auth_sid},
                                 headers={"x-csrf-token": token}
                                 )

        expected_fields = ["username",
                           "id",
                           "email",
                           "firstName",
                           "lastName"
                           ]
        Assertions.assert_json_has_keys(response2, expected_fields)


