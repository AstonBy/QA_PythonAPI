import allure
import requests
import random

from libconnect.assertions import Assertions
from libconnect.base_case import BaseCase
from libconnect.connect_requests import ConnectRequests



class TestAssessments(BaseCase):
    def test_happiness_assessment(self):
        # GETTING COOKIE WITH/WITHOUT USER'S DATA (default value)
        ses_cookie = self.get_cookie_via_login("qa06-connect.stage-twill.health")

        # PASSING THE HAPPINESS_ASSESSMENT DIALOG
        response_start_ha_dialog = ConnectRequests.send(
            "GET", "v1/users/dialog/ha/",
            cookies={"ses": ses_cookie})
        Assertions.assert_status_code(response_start_ha_dialog, 200)
        Assertions.assert_json_value_by_name(response_start_ha_dialog, "dialog_mode", "scheduled_assessment", "Another type OR no type for the HA dialog")
        conversation_id = self.get_json_value(response_start_ha_dialog, "conversation_id")
        turn_number = self.get_json_value(response_start_ha_dialog, "turn_number")
        options_HA = self.get_json_value(response_start_ha_dialog, "data")["options"]

        while True:
            if options_HA:
                client_input = options_HA[random.randrange(0, len(options_HA))]["id"]
            else:
                client_input = ""

            response_answers_ha = ConnectRequests.send("POST",
                "v1/users/dialog/",
                json={
                    "conversation_id": conversation_id,
                    "turn_number": turn_number,
                    "client_input": client_input
                },
                cookies={"ses": ses_cookie},
            )
            turn_number = self.get_json_value(response_answers_ha, "turn_number")
            options_HA = self.get_json_value(response_answers_ha, "data")["options"]

            Assertions.assert_status_code(response_answers_ha, 201)

            if self.get_json_value(response_answers_ha, "data")["end"] == True:
                break

        ha_new_score = self.get_json_value(response_answers_ha, "runtime_data")['variables'][-1]["value"]

        # CHECK HOMEPAGE LOADING
        response_home = ConnectRequests.send("GET",
                                             "v1/home/",
                                             cookies={"ses": ses_cookie})
        Assertions.assert_status_code(response_home, 200)
        happiness_scores_homepage = self.get_json_value(response_home, "happiness_scores")[0]['score']
        Assertions.assert_value1_equal_value2(ha_new_score, happiness_scores_homepage)

    def test_assessment_dialog(self):
        # GETTING COOKIE WITH/WITHOUT USER'S DATA (default value)
        ses_cookie = self.get_cookie_via_login("qa06-connect.stage-twill.health")

        # PASSING THE ONBOARDING_ASSESSMENT DIALOG
        response_start_assessment_dialog = ConnectRequests.send(
            "GET", "v1/users/dialog/",
            cookies={"ses": ses_cookie})
        Assertions.assert_status_code(response_start_assessment_dialog, 200)
        Assertions.assert_json_value_by_name(response_start_assessment_dialog, "dialog_mode", "onboarding_assessment", "Another type OR no type for the dialog")
        conversation_id = self.get_json_value(response_start_assessment_dialog, "conversation_id")
        turn_number = self.get_json_value(response_start_assessment_dialog, "turn_number")
        options = self.get_json_value(response_start_assessment_dialog, "data")["options"]

        while True:
            if options:
                client_input = options[random.randrange(0, len(options))]["id"]
            else:
                client_input = ""

            response_answers_assessment_dialog = ConnectRequests.send("POST",
                "v1/users/dialog/",
                json={
                    "conversation_id": conversation_id,
                    "turn_number": turn_number,
                    "client_input": client_input
                },
                cookies={"ses": ses_cookie}
            )

            turn_number = self.get_json_value(response_answers_assessment_dialog, "turn_number")
            options = self.get_json_value(response_answers_assessment_dialog, "data")["options"]

            if self.get_json_value(response_answers_assessment_dialog, "data")["end"] == True:
                break

        Assertions.assert_status_code(response_answers_assessment_dialog, 200)

        # CHECKING TRIAGE MODALITIES
        response_triage_modality = ConnectRequests.send("GET",
                                                        "v1/modalities/triage/",
                                                        cookies={"ses": ses_cookie})

        Assertions.assert_status_code(response_triage_modality, 200)
