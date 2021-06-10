from .pages.product_page import ProductPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

class TestNegativeChecks():

    @pytest.mark.xfail(reason="Element should be on page")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message_after_adding_product_to_basket()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()

    @pytest.mark.xfail(reason="Element should be on page")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.message_disappeared_after_adding_product_to_basket()