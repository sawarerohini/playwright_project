import self


class CheckoutPage:
    def __init__(self,page):
        self.page = page
        self._first_name = page.locator('[data-test="firstName"]')
        self._last_name = page.locator('[data-test="lastName"]')
        self._zip_code = page.locator('[data-test="postalCode"]')
        self._continue = page.locator("#continue")
        self._finish = page.locator("#finish")
        self._conform_message = page.locator("h2.complete-header")


    def enter_first_name(self,f_name):
        self._first_name.fill(f_name)
        return self

    def enter_last_name(self,l_name):
        self._last_name.fill(l_name)
        return self

    def enter_zip(self,code):
        self._zip_code.fill(code)
        return self

    def enter_checkout_detail(self,f_name,l_name,code):
        self.enter_first_name(f_name)\
            .enter_last_name(l_name)\
            .enter_zip(code)
        return self

    def click_continue(self):
        self._continue.click()
        return self

    def click_finish(self):
        self._finish.click()
        return self

    def get_conform_message(self):
        return self._conform_message