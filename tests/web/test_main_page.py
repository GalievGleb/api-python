import time
import allure
import pytest
from selenium import webdriver

from tests.web.pages.main_page_edit import Main_page_edit
from tests.web.pages.main_page_get import Main_page_get
from tests.web.pages.main_page_register import Main_page_register


# @allure.description("Test main page Selenium")
def test_main_web():
    print("\nStart Test 1")

    driver = webdriver.Chrome()
    driver.get("https://reqres.in/")

    mpr = Main_page_register(driver)
    mpr.api_register()

    mpg = Main_page_get(driver)
    mpg.api_login()

    mpe = Main_page_edit(driver)
    mpe.api_edit()

    driver.quit()
    print("Finish Test 1")
