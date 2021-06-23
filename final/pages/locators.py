from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini.pull-right > .btn-group a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    CHARS = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_INPUT = (By.ID, 'id_registration-email')
    PASSWORD_INPUT_ONE = (By.ID, 'id_registration-password1')
    PASSWORD_INPUT_TWO = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, 'registration_submit')


class BasketPageLocators():
    PRODUCTS_BLOCK = (By.ID, "basket_formset")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PAGE_BLOCK = (By.CLASS_NAME, "product_page")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success strong')
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_BUTTON_TEXT = (By.CSS_SELECTOR, ".basket-mini.pull-right")
