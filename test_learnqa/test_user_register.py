import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserRegister(BaseCase):
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data1 = self.prepare_registration_data(email)

        response = MyRequests.post(
            "/user/",
            data=data1)
        print(response.text)
        print(response.status_code)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", f"Unexpected error message"

    def test_create_user_successfully(self):
        data2 = self.prepare_registration_data()
        response = MyRequests.post(
            "/user/",
            data=data2)
        print(response.text)
        print(response.status_code)

        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_status_code(response, 200)