import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-GB, es, fr")

    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


# фикстура открытия/закрытия браузера, а также проверка на этапе формирования ссылки, что подставляется верный параметр language
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    user_language = request.config.getoption("language")
    return user_language
