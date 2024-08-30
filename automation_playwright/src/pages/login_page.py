
from automation_playwright.src.pages.product_page import ProductListPage

class LoginPage:
    def __init__(self,page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_text("Login")
        self._error_message = page.locator('//h3[@data-test="error"]')

    def enter_username(self,u_name):
        self._username.clear()
        self._username.fill(u_name)

    def enter_password(self,p_word):
        self._password.clear()
        self._password.fill(p_word)

    def login(self):
        self.login_btn.click()

    def do_login(self,credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.login()
        return ProductListPage(self.page)


    @property
    def err_msg_loc(self):
        return self._error_message


    @property
    def login_btn(self):
        return self._login_btn