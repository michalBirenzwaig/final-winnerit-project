from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page