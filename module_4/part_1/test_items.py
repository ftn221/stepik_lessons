#на случай, если ссылка сформирована верно, но страница по разным причинам не открылась
#реализована проверка текста кнопки для каждого языка. Если текст кнопки соответствует действительности
#тогда проверка пройдена и страница открыта корректно

def test_check_the_same_language(browser):
    button = browser.find_element_by_class_name("btn-add-to-basket").text

    if button == "Добавить в корзину":
        assert button == "Добавить в корзину", f"Your text in the button is '{button}'"
    elif button == "Add to basket":
        assert button == "Add to basket", f"Your text in the button is '{button}'"
    elif button == "Ajouter au panier":
        assert button == "Ajouter au panier", f"Your text in the button is '{button}'"
    elif button == "Añadir al carrito":
        assert button == "Añadir al carrito", f"Your text in the button is '{button}'"
    else:
        assert False, "Your language is not from list"