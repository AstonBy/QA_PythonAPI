import requests
from datetime import datetime
from lib.assertions import Assertions
from lib.base_case import BaseCase

class TestCreateNewUser(BaseCase):
    def test_new_user_create(self):
        domain = "example.ru"
        datetime_email = datetime.now().strftime("%d%m%Y%H%M%S")
        first_part_domain = "learnqa"
        email = f"{first_part_domain}{datetime_email}@{domain}"
        response = requests.post("https://playground.learnqa.ru/api/user/",
                             data= {
                                 "username": "Testing",
                                 "firstName": "John",
                                 "lastName": "Doe",
                                 "email": email,
                                 "password": "1234"
                             }
                             )
        Assertions.assert_status_code(response, 200)
        print(response.text)