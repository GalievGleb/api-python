from tests.web.pages.main_page_edit import Main_page_edit
from tests.web.pages.main_page_get import Main_page_get
from tests.web.pages.main_page_register import Main_page_register
from tests.api.test_user_edit import TestUserEdit
from tests.api.test_user_get import TestUserGet
from tests.api.test_user_register import TestUserRegister


# Импортируйте WebDriver
from selenium import webdriver

# Создайте экземпляр WebDriver (используйте нужный вам браузер)
driver = webdriver.Chrome()  # Пример для браузера Google Chrome

# Получаем JSON данные из API
response1 = TestUserEdit().test_edit_user()

# Создайте экземпляр класса Main_page_edit и передайте driver
main_page_edit_instance = Main_page_edit(driver)

# Получаем JSON данные из Selenium
response2 = main_page_edit_instance.text_get_create_json_list(response1)

# Функция для сравнения JSON данных
def compare_json(json1, json2):
    if json1 == json2:
        return True
    else:
        return False

# Вызываем функцию сравнения и выводим результат
if compare_json(response1, response2):
    print("JSON данные из обоих методов совпадают.")
else:
    print("JSON данные из обоих методов не совпадают.")

# Закрываем браузер после использования
driver.quit()

