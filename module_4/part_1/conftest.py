import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-GB, es, fr")

#фикстура открытия/закрытия браузера, а также проверка на этапе формирования ссылки, что подставляется верный параметр language
@pytest.fixture(scope="function")
def browser(request):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    browser.get(link)
    yield browser
    time.sleep(5)
    browser.quit()