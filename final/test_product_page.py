from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

# data
standart_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# Ссылка для 5 урока, шага 2, где нужно высчитывать по формуле и вводить во всплывающее окно
add_in_basket_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage():
    def test_check_math_on_product_page(self, browser):
        page = ProductPage(browser, add_in_basket_link)
        page.open()
        page.click_on_add_button()
        page.solve_quiz_and_get_code()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, language):
        page = ProductPage(browser, standart_link)
        basket_page = BasketPage(browser, standart_link)
        page.open()
        page.go_to_basket()
        basket_page.check_products_present()
        basket_page.check_message_basket_empty(language)

    @pytest.mark.parametrize('promo_offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                             pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    class TestProductPageWithParametrize():
        def test_guest_can_add_product_to_basket(self, browser, promo_offer):
            page = ProductPage(browser, f'{standart_link}?promo={promo_offer}')
            page.open()
            page.click_on_add_button()
            page.solve_quiz_and_get_code()
            page.check_the_product_name()
            page.check_the_product_price()

    @pytest.mark.xfail(reason="Element should be on page")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, standart_link)
        page.open()
        page.guest_cant_see_success_message_after_adding_product_to_basket()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, standart_link)
        page.open()
        page.guest_cant_see_success_message()

    @pytest.mark.xfail(reason="Element should be on page")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, standart_link)
        page.open()
        page.message_disappeared_after_adding_product_to_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, standart_link)
        page.open()
        login_page = LoginPage(browser, standart_link)
        page.go_to_login_page()
        email = login_page.generate_new_login()
        password = login_page.generate_new_password()
        login_page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, standart_link)
        page.guest_cant_see_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, standart_link)
        page.open()
        page.click_on_add_button()
        page.check_the_product_name()
        page.check_the_product_price()
