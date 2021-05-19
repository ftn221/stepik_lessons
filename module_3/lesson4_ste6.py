from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

browser = webdriver.Chrome()

browser.get(link)

thex = int(browser.find_element_by_id("input_value").text)

result = calc(thex)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true)", button)

robotCheckbox = browser.find_element_by_id("robotCheckbox")
robotCheckbox.click()

robotsRule = browser.find_element_by_id("robotsRule")
robotsRule.click()

button.click()