from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

browser = webdriver.Chrome()
browser.get(link)

login_url = browser.current_url

assert login_url == "http://selenium1py.pythonanywhere.com/ru/accounts/logiggggn/"