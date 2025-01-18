import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__username_field=page.locator('#user-name')
        self.__password_field=page.locator('#password')
        self.__login_button=page.get_by_role('button',name='Login')
        self.__error_message=page.locator("[data-test='error']")

    def navigate_to(self, url: str):
        with allure.step(f"Navigating to url: {url}"):
            self.__page.goto(url)

    def fill_username_field(self, username: str):
        with allure.step(f"Login to app with username: {username}"):
            self.__username_field.fill(username)

    def fill_password_field(self, password: str):
        with allure.step(f"Login to app with password: {password}"):
            self.__password_field.fill(password)

    def click_login_button(self):
        with allure.step("Click on login button"):
            self.__login_button.click()

    def validate_error_message(self, error_message: str):
        with allure.step(f"Validating that error message is: {error_message}"):
            expect(self.__error_message).to_contain_text(error_message)