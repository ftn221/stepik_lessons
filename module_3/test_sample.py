from selenium import webdriver

# Data
login_page = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

login = "ftn221@gmail.com"
password = "camaross425"
login_input_id = "id_login-username"
password_input_id = "id_login-password"
assert_phrase_of_success_message = "Рады видеть вас снова"
submit_button_name_for_search = "login_submit"
success_login_message_selector = ".alert-success .alertinner"

def test_entry_use_login_and_password():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page)

        # Act
        browser.find_element_by_id(login_input_id).send_keys(login)
        browser.find_element_by_id(password_input_id).send_keys(password)
        browser.find_element_by_name(submit_button_name_for_search).click()

        # Assert
        success_login_message = browser.find_element_by_css_selector(success_login_message_selector).text.strip()
        assert success_login_message == assert_phrase_of_success_message, "No message about success login"

    finally:
        browser.quit()

test_entry_use_login_and_password()