from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_user(self):
        register_data = self.edit_data()

        response1 = MyRequests.put("users/2", data=register_data)

        Assertions.assert_code_status(response1, 200)

        Assertions.assert_json_has_key(response1, "name")
        Assertions.assert_json_has_key(response1, "job")
        Assertions.assert_json_has_key(response1, "updatedAt")
        return response1.json()

    def test_edit_user_negative(self):
        register_data = self.edit_data()

        response2 = MyRequests.put("users/12test_negative", data=register_data)

        Assertions.assert_code_status(response2, 200)

        Assertions.assert_json_has_key(response2, "name")
        Assertions.assert_json_has_key(response2, "job")
        Assertions.assert_json_has_key(response2, "updatedAt")
