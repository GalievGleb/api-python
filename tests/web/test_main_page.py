import time
import allure
import pytest

from tests.web.pages.main_page_edit import Main_page_edit
from tests.web.pages.main_page_get import Main_page_get
from tests.web.pages.main_page_register import Main_page_register

@allure.description("Test buy product 1")
def test_buy_product_1(selenium_driver):
    print("\nStart Test 1")

    mpr = Main_page_register(selenium_driver)
    mpr.api_register()

    mpg = Main_page_get(selenium_driver)
    mpg.api_login()

    mpe = Main_page_edit(selenium_driver)
    mpe.api_edit()

    print("Finish Test 1")








