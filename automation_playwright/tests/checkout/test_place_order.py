from playwright.sync_api import sync_playwright, expect

from automation_playwright.src.pages.login_page import LoginPage


def test_place_order(set_up_tear_down) ->None:
    page = set_up_tear_down
    credentials = {'username':'standard_user','password':'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    product_name = "Sauce Labs Bolt T-Shirt"
    checkout_p = products_p.click_add_to_card(product_name)\
        .click_card_icon()\
        .click_checkout_button()\
        .enter_checkout_detail("ds","sdsa","23243")\
        .click_continue()\
        .click_finish()

    expect(checkout_p.get_conform_message()).to_have_text("Thank you for your order!")