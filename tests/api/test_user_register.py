from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):

    def test_create_user_successfull(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("register", data=data)

        assert response.status_code == 200, f"Unexpected` status code {response.status_code}"
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_unsuccessful(self):
        data = self.prepare_registration_data_negative()
        response = MyRequests.post("register", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == ('{"error":"Note: Only defined users succeed registration"}')
