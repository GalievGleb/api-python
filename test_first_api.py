import requests
import pytest


class TestFirstApi:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Gleb"
        data = {'name': name}

        response = requests.get(url, params=data) # Response [200]
        assert response.status_code == 200, "Wrong status code" #200

        response_dict = response.json() # {'answer': 'Hello, Gleb'}
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"] # Hello, Gleb
        assert expected_response_text == actual_response_text, f"Actual text in the response is not corrected"