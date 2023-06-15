import requests
import pytest


class TestFirstApi:
    names = [
        ("Gleb"),
        ("Regina"),
        ("")
    ]
    @pytest.mark.parametrize('name', names) # в name pytest передает данные, names переменная в которой данные хранятся
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}

        response = requests.get(url, params=data) # Response [200]
        assert response.status_code == 200, "Wrong status code" #200

        response_dict = response.json() # {'answer': 'Hello, Gleb'}
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"] # Hello, Gleb
        assert expected_response_text == actual_response_text, f"Actual text in the response is not corrected"