from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Укажите путь к исполняемому файлу ChromeDriver
chromedriver_path = "C:\\Users\\galie\\Desktop\\chromedriver.exe"

# Создаем экземпляр веб-драйвера (в данном случае, Chrome)
driver = webdriver.Chrome()

# Открываем веб-страницу Google
driver.get("https://www.google.com")

# Находим поисковое поле по его имени (в данном случае, 'q')
search_box = driver.find_element_by_name("q")

# Вводим поисковый запрос
search_box.send_keys("Python programming")

# Нажимаем клавишу Enter для выполнения поиска
search_box.send_keys(Keys.RETURN)

# Ждем несколько секунд, чтобы увидеть результаты


time.sleep(5)

# Закрываем веб-браузер
driver.quit()
