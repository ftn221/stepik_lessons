from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

trollface = browser.find_element_by_class_name("trollface")
trollface.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

input_value = int(browser.find_element_by_id("input_value").text)
result = calc(input_value)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

button = browser.find_element_by_tag_name("button")
button.click()