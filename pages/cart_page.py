from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__checkout_button = page.locator("[data-test=\"checkout\"]")

    def click_checkout_button(self):
        with allure.step("Click on checkout button"):
            self.__checkout_button.click()