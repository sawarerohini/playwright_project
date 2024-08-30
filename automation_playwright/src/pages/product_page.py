from automation_playwright.src.pages.cart_page import CartPage


class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._burger_menu = page.locator("button#react-burger-menu-btn")
        self._logout_btn = page.locator("#logout_sidebar_link")
        self._cart_icon = page.locator("a.shopping_cart_link")


    @property
    def product_header(self):
        return self._products_header

    def click_burger_menu_btn(self):
        self._burger_menu.click()

    def click_logout_btn(self):
        self._logout_btn.click()

    def do_logout(self):
        self.click_burger_menu_btn()
        self.do_logout()

    def get_add_remove_card_locator(self,product):
        return self.page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')

    def click_add_to_card(self,product):
        self.get_add_remove_card_locator(product).click()
        return self

    def click_card_icon(self):
        self._cart_icon.click()
        return CartPage(self.page)