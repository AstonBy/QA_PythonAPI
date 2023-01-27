import json
from datetime import datetime

import requests
from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f'Cannot find cookie with name {cookie_name} in the last response'
        return response.cookies[cookie_name]


    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f'Cannot find header with name {headers_name} in the last response'
        return response.headers[headers_name]


    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not JSON format. Response text is {response.text}'
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]

    def prepare_reg_email(self, email=None):
        if email is None:
            email_main_part = "shkorkin+qa06"
            random_email_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email_domain = "alarstudios.com"
            email = f"{email_main_part}{random_email_part}@{email_domain}"

        return {
            "email": email,
            "password": "1234qwertY!",
            "username": "Ast"
        }

    def get_ses_cookie(self, url: str, json: dict = None):

        # GETTING CLIENT_ID FOR THE ENV
        client_id_response = requests.get(
            f"https://{url}/assets/config/{url}.json")
        assert client_id_response.status_code == 200, f"Status code should be 200, but it is {client_id_response.status_code}"
        client_id = self.get_json_value(client_id_response, "client_id")

        # RESPONSE TO THE AUTH SERVER
        response_to_auth = requests.post(
            f"https://qa06-auth.stage-twill.health/api/public/auth/?client_id={client_id}",
            json=json)
        assert response_to_auth.status_code == 200, f"Status code should be 200, but it is {response_to_auth.status_code}"
        access_token = self.get_json_value(response_to_auth, "access_token")

        # GET SES COOKIE FROM THE /users/me/ ENDPOINT
        response_user_me = requests.get(f"https://{url}/api/v1/users/me/?access_token={access_token}")
        assert response_user_me.status_code == 200, f"Status code should be 200, but it is {response_user_me.status_code}"
        ses_cookie = self.get_cookie(response_user_me, "ses")

        return ses_cookie

    def get_cookie_via_login(self, url: str, json: dict = None):   # Local/global variable is required
        if json is None:
            json = {"email": "shkorkin+qa06connect@alarstudios.com",
                "password": "1234qwertY!"}

        return self.get_ses_cookie(url, json)



