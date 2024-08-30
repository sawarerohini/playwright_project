from playwright.sync_api import sync_playwright, expect

from automation_playwright.src.pages.login_page import LoginPage


def test_add_to_card(set_up_tear_down, get_add_remove_card_locator=None) ->None:
    page = set_up_tear_down
    credentials = {'username':'standard_user','password':'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    product_name = "Sauce Labs Backpack"
    products_p.click_add_to_card(product_name)
    expect(products_p.get_add_remove_card_locator(product_name)).to_have_text('text="Remove"')
