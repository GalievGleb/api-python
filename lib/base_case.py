import json.decoder

from requests import Response
from datetime import datetime


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with the name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON Format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self):
        return {
            'email': 'eve.holt@reqres.in',
            'password': 'pistol'

        }

    def edit_data(self):
        return {
            "name": "Gleb",
            "job": "zion resident"
        }

    def prepare_registration_data_negative(self):
        return {
            'email': 'FergusAndersen@reqres.in',
            'password': 'Nope'
        }
