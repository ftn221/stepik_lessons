from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def click_on_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def check_the_product_name(self):
        product_name = self.browser.find_element(By.TAG_NAME, "h1").text
        product_name_on_message = self.browser.find_element(By.XPATH, f'//strong[text()="{product_name}"]').text
        assert product_name == product_name_on_message, "Имена в заголовке товара и сообщении, не совпадают"

    def check_the_product_price(self):
        product_price = self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text
        link_on_basket_text = self.browser.find_element(By.CSS_SELECTOR, ".basket-mini.pull-right").text.strip()
        assert link_on_basket_text.find(product_price) != -1