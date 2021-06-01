import random

#функция для рандомного получения логина и пароля
def random_chars():
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    random_word = ""
    for n in range(10):
        random_word += random.choice(chars)
    return random_word

def test_registration_user(browser):
    #поиск кнопки перехода на страницу регистрации
    login_link = browser.find_element_by_id("login_link")
    login_link.click()

    #поиск инпута email и формирование адреса почты из рандомного слова плюс добавления @mail.com в конце
    registration_email_input = browser.find_element_by_id("id_registration-email")
    user_email = f"{random_chars()}@mail.com"
    registration_email_input.send_keys(user_email)

    #поиск инпутов паролей, формирование самих рандомных паролей и их ввод
    password_one_input = browser.find_element_by_id("id_registration-password1")
    password_two_input = browser.find_element_by_id("id_registration-password2")
    user_password = random_chars()
    password_one_input.send_keys(user_password)
    password_two_input.send_keys(user_password)

    #поиск кнопки регистрации и клик на нее
    submit_button = browser.find_element_by_name("registration_submit")
    submit_button.click()

    #реализовал проверку, при которой ищется блок с сообщением об успешной регистрации
    #если блок не найден, выбрасывается assertionError с сообщением, о непрохождении регистрации
    # сделан именно поиск блока с сообщением об успехе, а не assert с проверкой фразы, так как сайт многоязычный
    # и проверка русской фразы не проходила бы проверку у английской фразы, а так код универсален
    try:
        #ищем блок с сообщением об успехе
        browser.find_element_by_class_name("alertinner")

        # для удобства пользователя, вывод в консоль логина и пароля для дальнейшего входа
        print(f"Вы успешно зарегистрированы!\nВаш логин: \n{user_email}\nВаш пароль:\n{user_password}")
    except:
        assert 1 == 0, "Сообщение об успешной регистрации не было найдено"


