from automation_playwright.src.pages.checkout_page import CheckoutPage


class CartPage:
    def __init__(self,page):
        self.page = page
        self.checkout_btn = page.locator("#checkout")

    def click_checkout_button(self):
        self.checkout_btn.click()
        return CheckoutPage(self.page)