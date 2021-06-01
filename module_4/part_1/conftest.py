import pytest
from selenium import webdriver

#добавляем распознавание текста в коммандную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en-gb, es, fr")

#фикстура открытия/закрытия браузера, а также проверка на этапе формирования ссылки, что подставляется верный параметр language
@pytest.fixture(scope="function")
def browser(request):

    language_param = request.config.getoption("language")
    if language_param == "ru":
        link = f"http://selenium1py.pythonanywhere.com/{language_param}/catalogue/coders-at-work_207/"
    elif language_param == "en-gb":
        link = f"http://selenium1py.pythonanywhere.com/{language_param}/catalogue/coders-at-work_207/"
    elif language_param == "es":
        link = f"http://selenium1py.pythonanywhere.com/{language_param}/catalogue/coders-at-work_207/"
    elif language_param == "fr":
        link = f"http://selenium1py.pythonanywhere.com/{language_param}/catalogue/coders-at-work_207/"
    else:
        assert False, "Language in command line is not ru, en-gb, fr or es"
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    browser.quit()