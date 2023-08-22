import time
import allure
import pytest
from tests.web.pages.main_page_register import Main_page

@allure.description("Test buy product 1")
def test_buy_product_1(selenium_driver):
    print("\nStart Test 1")

    mp = Main_page(selenium_driver)
    mp.product_confirmation()

    print("Finish Test 1")








