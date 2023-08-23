import pytest
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def web_driver():
    driver = webdriver.Chrome()
    driver.get("https://reqres.in/")  # Эту строку можно настроить для разных тестовых URL
    yield driver  # Возвращаем WebDriver в тестовую функцию
    driver.quit()  # Закрываем WebDriver после завершения теста
