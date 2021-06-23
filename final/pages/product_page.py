from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def click_on_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def check_the_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_on_message = self.browser.find_element(By.XPATH, f'//strong[text()="{product_name}"]').text
        assert product_name == product_name_on_message, "Name on product title and message not same"

    def check_the_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_button_text = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON_TEXT).text.strip()
        assert basket_button_text.find(product_price) != -1

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Element present on page'

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Element present on page'

    def message_disappeared_after_adding_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Element is not disappeared'
