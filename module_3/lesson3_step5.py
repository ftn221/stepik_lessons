from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get(link)

input_value = browser.find_element_by_id("input_value").text
answer = calc(input_value)

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(answer)

robotCheckbox = browser.find_element_by_id("robotCheckbox")
robotCheckbox.click()

robotsRule = browser.find_element_by_id("robotsRule")
robotsRule.click()

button = browser.find_element_by_tag_name("button")
button.click()