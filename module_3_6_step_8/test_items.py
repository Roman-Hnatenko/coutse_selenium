import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button_exists(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(
    	".product_page #add_to_basket_form .btn-add-to-basket"
    	)

    assert button, "Button has not been found."
