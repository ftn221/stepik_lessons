import pytest
from selenium import webdriver

#добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en-gb, es, fr")

#добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser")

#фикстура открытия/закрытия браузера, а также проверка на этапе формирования ссылки, что подставляется верный параметр language
@pytest.fixture(scope="function")
def browser(request):

    language_param = request.config.getoption("language")
    browser_param = request.config.getoption("browser_name")

    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    browser.quit()