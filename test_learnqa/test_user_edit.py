from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # CREATE
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/",
            data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        first_name = register_data["firstName"]
        print(first_name)
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {"email": email,
                      "password": password
                      }

        response2 = MyRequests.post("/user/login",
            data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        print(response2.cookies)
        print(response2.headers)
        print(response2.text)

        Assertions.assert_status_code(response2, 200)

        # EDIT
        new_name = "Artur"
        response3 = MyRequests.put(f"/user/{user_id}",
                                 cookies={"auth_sid": auth_sid},
                                 headers={"x-csrf-token": token},
                                 data={"firstName": new_name}
                                 )
        Assertions.assert_status_code(response3, 200)
        print(response3.cookies)
        print(response3.headers)
        print(response3.text)

        # CHECK

        response4 = MyRequests.get(f"/user/{user_id}",
                                 cookies={"auth_sid": auth_sid},
                                 headers={"x-csrf-token": token}
                                 )
        print(response4.cookies)
        print(response4.headers)
        print(response4.text)
        Assertions.assert_status_code(response4, 200)
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, f"First name is not changed after the edit")