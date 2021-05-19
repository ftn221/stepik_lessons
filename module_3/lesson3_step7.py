from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

attr_container = browser.find_element_by_id("treasure")
valuex = attr_container.get_attribute("valuex")

result = calc(valuex)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

robotCheckbox = browser.find_element_by_id("robotCheckbox")
robotCheckbox.click()

robotsRule = browser.find_element_by_id("robotsRule")
robotsRule.click()

button = browser.find_element_by_tag_name("button")
button.click()