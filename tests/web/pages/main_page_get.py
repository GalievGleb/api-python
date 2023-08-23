from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.base_class import Base


class Main_page_get(Base):
    url = 'https://reqres.in/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_get_button = "//li[@data-id='login-successful']"
    create_json_login = "//pre[@data-key='output-response']"

    # Getters

    def get_login_get_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_get_button)))

    def get_create_json_login(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.create_json_login)))

    # Action

    def click_login_get_button(self):
        self.get_login_get_button().click()
        print("Click GET login button")

    def text_get_create_json_login(self):
        text = self.get_create_json_login().text
        print("Get text json_login create_selenium")
        return text

    # Methods
    def api_login(self):
        self.get_current_url()
        self.click_login_get_button()
        self.text_get_create_json_login()
