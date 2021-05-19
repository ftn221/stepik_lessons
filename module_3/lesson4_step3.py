from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()

browser.get(link)

num_one = int(browser.find_element_by_id("num1").text)
num_two = int(browser.find_element_by_id("num2").text)
sum = str(num_one + num_two)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(sum)

button = browser.find_element_by_tag_name("button")
button.click()