import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.base_class import Base


# from utilities.logger import logger


class Main_page(Base):
    url = 'https://reqres.in/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    create_button = "//li[@data-id='post']"
    create_json = "//pre[@data-key='output-response']"

    # Getters

    def get_create_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.create_button)))

    def get_create_json(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.create_json)))

    # Action

    def click_create_button(self):
        self.get_create_button().click()
        print("Click create button")

    def text_get_create_json(self):
        text = self.get_create_json().text
        print("Get text json create_selenium")
        return text

    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_create_button()
        self.text_get_create_json()

driver = webdriver.Chrome()
driver.get("https://reqres.in/")  # Замените URL на нужный
mp = Main_page(driver)
mp.product_confirmation()
driver.quit()
