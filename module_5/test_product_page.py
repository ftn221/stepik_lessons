from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

class TestProductPage():
    def test_check_math_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.click_on_add_button()
        page.solve_quiz_and_get_code()