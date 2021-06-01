import unittest
from selenium import webdriver

link_one = "http://suninjuly.github.io/registration1.html"
link_two = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link_one)

            # Ваш код, который заполняет обязательные поля
            first_name = browser.find_element_by_css_selector(".first_block .first")
            first_name.send_keys("first")

            last_name = browser.find_element_by_css_selector(".first_block .second")
            last_name.send_keys("last")

            email_input = browser.find_element_by_css_selector(".first_block .third")
            email_input.send_keys("email")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "No welcome text")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_abs2(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link_two)

            # Ваш код, который заполняет обязательные поля
            first_name = browser.find_element_by_css_selector(".first_block .first")
            first_name.send_keys("first")

            last_name = browser.find_element_by_css_selector(".first_block .second")
            last_name.send_keys("last")

            email_input = browser.find_element_by_css_selector(".first_block .third")
            email_input.send_keys("email")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "No welcome text")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()