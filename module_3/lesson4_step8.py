from selenium import  webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element_by_name("firstname")
first_name.send_keys("niyaz")
last_name = browser.find_element_by_name("lastname")
last_name.send_keys("fazulzianov")
email = browser.find_element_by_name("email")
email.send_keys("blablabla")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_input = browser.find_element_by_id("file")
file_path = os.path.join(current_dir, "test_file.txt")
file_input.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()




