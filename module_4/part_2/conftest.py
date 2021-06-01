import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)
    browser.implicitly_wait(15)
    yield browser
    browser.quit()