from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def should_be_login_url(self):
        my_url = self.browser.current_url
        assert my_url.find('login') != -1, "Ваша подстрока не содержит слова login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Элемент login Form не найден"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Элемент login Form не найден"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def generate_new_login(self):
        email = f'{self.generate_new_word(8)}@fakemail.com'
        return email

    def generate_new_password(self):
        password = self.generate_new_word(12)
        return password

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input_one = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_ONE)
        password_input_two = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_TWO)
        password_input_one.send_keys(password)
        password_input_two.send_keys(password)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        registration_submit_button.click()
