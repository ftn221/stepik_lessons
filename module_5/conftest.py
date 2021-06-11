import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-GB, es, fr")

#фикстура открытия/закрытия браузера, а также проверка на этапе формирования ссылки, что подставляется верный параметр language
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def language(request):
    user_language = request.config.getoption("language")
    return user_language