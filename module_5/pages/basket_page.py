from .base_page import BasePage
from .locators import BasketPageLocators

#data
basket_empty_messages = {
    'en-GB': 'Your basket is empty',
    'ru': 'Ваша корзина пуста',
    'fr': 'Votre panier est vide',
    'es': 'Tu carrito esta vacío'
}

class BasketPage(BasePage):
    def check_products_present(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_BLOCK), "On the page have a products"

    def check_message_basket_empty(self, language):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        my_message = basket_empty_messages[language]
        assert empty_message.find(my_message) != -1, 'Basket empty message not find'