import random
import requests
from lib.base_case import BaseCase


class TestHA(BaseCase):
    def setup(self):
        data = {
            "email": "shkorkin+dev060922@alarstudios.com",
            "password": "1234qwertY!",
        }
        response1 = requests.post(
            "https://qa02.happify.com/api/public/auth/?client_id=gAAAAABjEKz0b2Mp8ng0LyWd2Bh6cNiOztr8EpLmBEQqdfKp_ENEl6MI37phWegTR5w9lPXn1ldNo3_0YOuH6bfbMJMbmuO5Fw==",
            json=data,
        )
        assert 'access_token' in response1.json(), 'There is no access_token, check email/password'

        self.access_token = response1.json()["access_token"]
        print(self.access_token)
        response2 = requests.get(
            "https://dev-connect.happify.com/api/v1/users/me/",
            params={"access_token": self.access_token},
        )
        assert 'ses' in response2.cookies, 'There is no SES cookie in the response'
        self.ses = response2.cookies.get("ses")
        print(self.ses)

    def test_ha(self):
        response3 = requests.get(
            "https://dev-connect.happify.com/api/v1/users/dialog/ha/",
            cookies={"ses": self.ses},
            )

        print(response3.text)

        conversation_id = response3.json()["conversation_id"]
        print(conversation_id)

        turn_number = 0
        while True:
            turn_number += 1
            response = requests.post(
                "https://dev-connect.happify.com/api/v1/users/dialog/",
                json={
                    "conversation_id": conversation_id,
                    "turn_number": turn_number,
                    "client_input": random.randint(1, 3),
                },
                cookies={"ses": self.ses},
            )
            print(response.text)
            if response.status_code != 200:
                break

        response_result = requests.get(
            "https://dev-connect.happify.com/api/v1/home/", cookies={"ses": self.ses}
        )
        print(response_result.text)

b = BaseCase
dir(b)