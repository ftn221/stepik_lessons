from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = browser.find_element_by_id("price")

WebDriverWait(browser, 30).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

book = browser.find_element_by_id("book")
book.click()

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

input_value = int(browser.find_element(By.ID, "input_value").text)

result = calc(input_value)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

button = browser.find_element_by_id("solve")
button.click()