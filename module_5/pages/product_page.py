from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_on_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def check_present_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE_BLOCK), "Product page is not present"