from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('promo_offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
class TestProductPageWithParametrize():
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        page = ProductPage(browser, f'{link}?promo={promo_offer}')
        page.open()
        page.click_on_add_button()
        page.solve_quiz_and_get_code()
        page.check_the_product_name()
        page.check_the_product_price()