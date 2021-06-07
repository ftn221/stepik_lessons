# data
#словарь со значениями язык: текст на кнопке
languages_and_button_text_for_them = {
        'en-GB': "Add to basket",
        'ru': "Добавить в корзину",
        'fr': "Ajouter au panier",
        'es': "Añadir al carrito"
    }

def test_check_the_same_language(browser):
    # act
    #импорт делается не в начале файла, а здесь, чтобы получить актуальное значение языка. Если делать сразу, значение получается None
    from conftest import user_language

    #Получение текста из кнопки
    button_text = browser.find_element_by_class_name("btn-add-to-basket").text

    # assert
    # получаем значение соответствующее ключу в виде пользовательского языка
    assert languages_and_button_text_for_them.get(user_language) == button_text, 'Текст на кнопке не соответствует значению текста кнопки для данного языка'