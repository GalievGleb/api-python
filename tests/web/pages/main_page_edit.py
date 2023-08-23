from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.base_class import Base


class Main_page_edit(Base):
    url = 'https://reqres.in/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    create_button_list = "//li[@data-id='users-single']"
    create_json_list = "//pre[@data-key='output-response']"

    # Getters

    def get_create_button_list(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.create_button_list)))

    def get_create_json_list(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.create_json_list)))

    # Action

    def click_create_button_list(self):
        self.get_create_button_list().click()
        print("Click create json button")

    def text_get_create_json_list(self):
        text = self.get_create_json_list().text
        print("Get text json_list selenium")
        return text

    # Methods
    def api_edit(self):
        self.get_current_url()
        self.click_create_button_list()
        self.text_get_create_json_list()
