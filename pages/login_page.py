from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__username_field=page.locator('#user-name')
        self.__password_field=page.locator('#password')
        self.__login_button=page.get_by_role('button',name='Login')

    def navigate_to(self, url: str):
            self.__page.goto(url)

    def login_to_application(self, username: str, password: str):
        self.__username_field.fill(username)
        self.__password_field.fill(password)
        self.__login_button.click()