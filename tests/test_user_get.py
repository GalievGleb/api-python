from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("users/2")

        Assertions.assert_json_has_key(response, "data")
        Assertions.assert_json_has_key(response, "support")
        Assertions.assert_json_has_not_key(response, "password")
        Assertions.assert_json_has_not_key(response, "login")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'eve.holt@reqres.in',
            'password': 'cityslicka'
        }

        response1 = MyRequests.post("login", data=data)

        Assertions.assert_json_has_key(response1, "token")
