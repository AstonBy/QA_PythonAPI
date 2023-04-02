import json
import pytest
import requests

class TestApiHello:
    names = [
        ("Evgeniy"),
        ("Kate"),
        (""),
        ("MarK"),
        ("Oleg"),
        ("Артур"),
        ()
    ]

    @pytest.mark.parametrize("name", names)
    def test_say_hello(self, name):
        params = {"name": name}
        response = requests.get("https://playground.learnqa.ru/api/hello", params=params)
        assert response.status_code == 200, f"Чёт пошло не так. Вместо 200 появилась {response.status_code}"

        assert "answer" in response.json(), f"Фигня с ключами"

        if name != '':
            assert json.loads(response.text)['answer'] == f"Hello, {params['name']}", f"Чёт не то с именем"
            print(json.loads(response.text)['answer'])
        else:
            assert json.loads(response.text)['answer'] == f"Hello, someone", f"Чёт с пустым именем не то"
            print("Hello, someone")