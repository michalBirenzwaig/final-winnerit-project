from playwright.sync_api import Page, expect
import utils.configs as configs
import allure

@allure.feature("login")
def test_successful_login(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()
    login_page.validate_url(configs.products_url)

@allure.feature("login")
def test_password_missing(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.click_login_button()
    login_page.validate_error_message("Password is required")

@allure.feature("login")
def test_access_check(login_page):
    login_page.navigate_to(configs.products_url)
    login_page.validate_url(configs.base_url)
    login_page.validate_error_message("You can only access '/inventory.html' when you are logged in.")

@allure.feature("login")
def test_refresh_page(page: Page,login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()
    page.reload(wait_until="load")
    login_page.validate_url(configs.products_url)
