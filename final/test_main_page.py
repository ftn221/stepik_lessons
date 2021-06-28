from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        page.open()
        # Assert
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        page.open()
        # Assert
        page.should_be_login_link()

    def test_should_be_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        login_page = LoginPage(browser, link)
        # Act
        page.open()
        page.go_to_login_page()
        # Assert
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, language):
        # Arrange
        page = MainPage(browser, link)
        basket_page = BasketPage(browser, link)
        # Act
        page.open()
        page.go_to_basket()
        # Assert
        basket_page.check_products_present()
        basket_page.check_message_basket_empty(language)

    @pytest.mark.personal_tests
    def test_guest_can_see_search_input(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        page.open()
        # Assert
        page.is_search_element_present()
