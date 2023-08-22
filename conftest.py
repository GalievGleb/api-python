import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def selenium_driver(request):
    # Создаем экземпляр веб-драйвера (в данном случае, Chrome)
    driver = webdriver.Chrome()

    def finalizer():
        # Закрываем драйвер после использования
        driver.quit()

    request.addfinalizer(finalizer)

    return driver

