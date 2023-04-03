import allure

from libconnect.base_case import BaseCase
from libconnect.connect_requests import ConnectRequests
from libconnect.assertions import Assertions

class TestHomepage(BaseCase):
    def test_homepage_loading(self):
        # GETTING COOKIE WITH/WITHOUT USER'S DATA (default value)
        ses_cookie = self.get_cookie_via_login("qa06-connect.stage-twill.health")
        # HOMEPAGE CHECK
        response_homepage = ConnectRequests.send(
            "GET",
            "v1/home/",
            cookies={"ses": ses_cookie})
        Assertions.assert_status_code(response_homepage, 200)
        homepage_elements = [
            "pages",
            "modalities",
            "happify_daily",
            "happiness_scores",
            "user_space"
        ]
        Assertions.assert_json_has_keys(response_homepage, homepage_elements)