import allure
import requests

from libconnect.assertions import Assertions
from libconnect.base_case import BaseCase
from libconnect.connect_requests import ConnectRequests

@allure.epic("Login Case(s)")
class TestLoginConnect(BaseCase):
    @allure.description("Test login feature")
    def test_login_connect(self):
        # GETTING COOKIE WITH/WITHOUT USER'S DATA (default value)
        ses_cookie = self.get_cookie_via_login("qa06-connect.stage-twill.health")
        # GETTING USER DATA
        response_users_me = ConnectRequests.send("GET",
                                                 "v1/users/me/",
                                                 cookies={"ses": ses_cookie})
        Assertions.assert_status_code(response_users_me, 200)
        user_data = [
            "id",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "phone",
            "zip_code",
            "partner_user_id",
            "username",
            "person_type",
            "receive_emails",
            "wcag_hight_contrast",
            "wcag_audio_inform",
            "wcag_disable_animation",
            "assessment_complite"]

        Assertions.assert_json_has_keys(response_users_me, user_data)

    # def test_login
