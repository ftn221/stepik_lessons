from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def click_on_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def check_the_name(self):
        title_text = self.browser.find_element(By.TAG_NAME, "h1").text
        print(title_text)
