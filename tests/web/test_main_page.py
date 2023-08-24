from tests.web.pages.main_page_edit import Main_page_edit
from tests.web.pages.main_page_get import Main_page_get
from tests.web.pages.main_page_register import Main_page_register

def test_main_web(web_driver):
    print("\nStart Test main web 1")

    mpr = Main_page_register(web_driver)
    mpr.api_register()

    mpg = Main_page_get(web_driver)
    mpg.api_login()

    mpe = Main_page_edit(web_driver)
    mpe.api_edit()

    print("Finish Test main web 1")
