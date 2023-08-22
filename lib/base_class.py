import datetime
from assertpy import assert_that


class Base():

    def __init__(self, driver):
        self.driver = driver

        """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

        """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

        """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\galie\\Desktop\\Project_Aut\\Project_Automation\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Сравнение JSON"""

    def compare_json(self, expected_json_str, actual_json_str):
        expected_json = json.loads(expected_json_str)
        actual_json = json.loads(actual_json_str)

        assert_that(actual_json).is_equal_to(expected_json)
        print("JSON comparison successful")
