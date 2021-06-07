import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# data
user_language = None
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-GB, es, fr")

#фикстура открытия/закрытия браузера, а также проверка на этапе формирования ссылки, что подставляется верный параметр language
@pytest.fixture(scope="function")
def browser(request):
    # arrange
    # нужна запись в глобальную переменную, чтобы была возможность считать ее в другом файле
    global user_language
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)
    browser.get(link)

    yield browser
    browser.quit()