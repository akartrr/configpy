import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_open_link(browser):
    browser.maximize_window()
    browser.get(link)

    button = browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button, "There is no Add to basket button!"

    time.sleep(20)
