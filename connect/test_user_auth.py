import json
from datetime import datetime
import allure
from libconnect.assertions import Assertions
from libconnect.base_case import BaseCase
from libconnect.connect_requests import ConnectRequests
import requests
import pytest

@allure.epic("Authorization cases")
class TestUserAuth(BaseCase):
    @allure.description("Sign-up a new user")
    def test_user_auth(self):
        # GETTING Employer_ID FIELDS
        response_group_access_field = ConnectRequests.send("GET", "v1/users/group-access-field/")   # Getting Employer_ID fields

        Assertions.assert_status_code(response_group_access_field, 200)
        Assertions.assert_json_has_key(response_group_access_field, 'is_signup_access_key')

        # ENTERING THE ACCESS CODE (Employer ID) AND GETTING THE group_id QUERY PARAM
        account_number = '123456789'   # Need an update
        response_group_fields_request = ConnectRequests.send("GET", f"v1/users/group-fields-request/?account_number={account_number}")

        Assertions.assert_status_code(response_group_fields_request, 200)
        Assertions.assert_json_has_key(response_group_fields_request, 'group_id')

        group_id = self.get_json_value(response_group_fields_request, "group_id")

        data = {
            "connect_form_data": {
                     'person_type': 'Employee',
                     'first_name': 'Ast',
                     'last_name': 'Metest',
                     'gender': 'Male',
                     'date_of_birth': '2000-01-09'},
            "form_data": {}
        }

        # INTERMEDIATE STEP (GROUP VALIDATION) AND GETTING THE 'ceu' COOKIE
        response_group_validate = ConnectRequests.send("POST",
            f"v1/users/group-validate/?group_id={group_id}",
            json=data)

        # with allure.step(f"{method} request to URL '{url}'"):
        #     response_group_validate = requests.request("POST", url_full, json=json)

        Assertions.assert_status_code(response_group_validate, 200)

        ceu = self.get_cookie(response_group_validate, "ceu")

        # USER'S SIGN UP
        email_for_registration = self.prepare_reg_email()
        response_register = ConnectRequests.send("POST", "v1/users/register/",
                                  json=email_for_registration,
                                  cookies={
                                      "ceu": ceu
                                  }
                                  )
        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, "access_token")
        access_token = self.get_json_value(response_register, "access_token")   # ???

        ses_cookie = self.get_cookie(response_register, "ses")

        # GETTING A NEW USER DATA
        response_users_me = ConnectRequests.send("GET", "v1/users/me/", cookies={"ses": ses_cookie})

        Assertions.assert_status_code(response_users_me, 200)
        Assertions.assert_json_has_keys(response_users_me,
                                        names=[
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
                                            "assessment_complite"
                                        ])

        user_email = self.get_json_value(response_users_me, "email")
        Assertions.assert_json_value_by_name(response_users_me, 'email', email_for_registration["email"], "User's email is not equal to the registration email")
        user_id = self.get_json_value(response_users_me, "id")
