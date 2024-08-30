from playwright.async_api import expect

from automation_playwright.src.pages.login_page import LoginPage


def test_logout(set_up_tear_down) ->None:
    page = set_up_tear_down
    credentials = {'username':'standard_user','password':'secret_sauce'}
    login_p = LoginPage(page)
    product_p = login_p.do_login(credentials)
    product_p.do_logout()
    expect(login_p.login_btn).to_be_visible()

