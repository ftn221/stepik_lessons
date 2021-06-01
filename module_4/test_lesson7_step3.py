import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_hello_goodbye(browser, link):
    browser.get(link)
    answer = str(math.log(int(time.time())))
    textarea = browser.find_element_by_tag_name("textarea")
    textarea.send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    check_message = browser.find_element_by_class_name("smart-hints__hint").text
    assert check_message == "Correct!", f"The check message is '{check_message}'"