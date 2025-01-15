from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__subtotal_label = page.locator('[data-test="subtotal-label"]')
        self.__finish_button=page.get_by_role('button',name='finish')

    def get_subtotal(self):
        return float(self.__subtotal_label.inner_text().replace("Item total: $", ""))

    def click_finish(self):
        self.__finish_button.click()
