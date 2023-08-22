import time
import allure
import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.main_page_register import Main_page



@allure.description("Test buy product 1")
def test_buy_product_1(set_grope):  # создаем метод
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\galie\\Desktop',
        chrome_options=options)  # Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром

    print("\nStart Test 1")

    mp = Main_page(driver)
    mp.product_confirmation()

    print("Finish Test 1")
    time.sleep(1)

