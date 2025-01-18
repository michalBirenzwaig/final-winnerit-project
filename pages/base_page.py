from playwright.sync_api import Page, expect
import allure

class BasePage:
    def __init__(self, page: Page):
        self.__page = page

    def validate_url(self, page_url: str):
        with allure.step(f"Validating that url is: {page_url}"):
            expect(self.__page).to_have_url(page_url)