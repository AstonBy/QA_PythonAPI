import pytest
import requests


class TestUserAuth:

    exclude_params = [("no_cookie"), ("no_token")]

    def setup(self):
        data = {"email": "vinkotov@example.com", "password": "1234"}
        response1 = requests.post(
            "https://playground.learnqa.ru/api/user/login", data=data
        )

        assert "auth_sid" in response1.cookies, "Нету ауз куки, проверьте Логин/Пароль"
        assert "x-csrf-token" in response1.headers, "Нету x-csrf токена"
        assert "user_id" in response1.json(), "Нету ID юзера"

        self.auth_sid_for_auth = response1.cookies["auth_sid"]
        self.x_csrf_token = response1.headers["x-csrf-token"]
        self.user_id = response1.json()["user_id"]

    def test_user_auth(self):

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            cookies={"auth_sid": self.auth_sid_for_auth},
            headers={"x-csrf-token": self.x_csrf_token},
        )
        print(response2.text)

        assert "user_id" in response2.json(), "User_id нет в Response2"

        self.user_id_check = response2.json()["user_id"]

        assert self.user_id_check == self.user_id, "Юзер не авторизован"

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_user_auth(self, condition):
        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.x_csrf_token},
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid_for_auth},
            )

        assert "user_id" in response2.json()

        self.user_id_check = response2.json()["user_id"]

        assert self.user_id_check == 0, f"Сервер отдал user_id без {condition}"
