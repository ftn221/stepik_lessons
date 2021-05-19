from selenium import webdriver
import math

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

want_button = browser.find_element_by_class_name("btn-primary")
want_button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

input_value = int(browser.find_element_by_id("input_value").text)
result = calc(input_value)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

submit_button = browser.find_element_by_tag_name("button")
submit_button.click()