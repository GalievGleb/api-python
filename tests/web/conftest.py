import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def web_driver():
    driver = webdriver.Chrome()
    driver.get("https://reqres.in/")
    yield driver
    driver.quit()
