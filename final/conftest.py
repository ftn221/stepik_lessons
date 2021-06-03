import pytest
from selenium import webdriver

#добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-GB, es, fr")

#добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser")

#фикстура открытия/закрытия браузера, а также проверка на этапе формирования ссылки, что подставляется верный параметр language
@pytest.fixture(scope="function")
def browser(request):
    link = ""
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    browser.get(link)
    yield browser
    browser.quit()