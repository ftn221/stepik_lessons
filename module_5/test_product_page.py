from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

class TestProductPage():
    def test_check_math_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.check_present_product_page()
        page.click_on_add_button()
        page.solve_quiz_and_get_code()
        time.sleep(10)