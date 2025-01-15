from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__checkout_button = page.locator("[data-test=\"checkout\"]")

    def click_checkout_button(self):
        self.__checkout_button.click()