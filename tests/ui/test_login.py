from playwright.sync_api import Page, expect
import utils.configs as configs
import allure

# טסט התחברות מוצלחת
@allure.feature("login")
def test_successful_login(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()
    login_page.validate_url(configs.products_url)

# טסט לוגין ללא סיסמא
@allure.feature("login")
def test_password_missing(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.click_login_button()
    login_page.validate_error_message("Password is required")

# טסט לוגין ללא שם משתמש
@allure.feature("login")
def test_username_missing(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()
    login_page.validate_error_message("Username is required")

# טסט שמנסה לעקוף כניסה למערכת
@allure.feature("login")
def test_access_check(login_page):
    login_page.navigate_to(configs.products_url)
    login_page.validate_url(configs.base_url)
    login_page.validate_error_message("You can only access '/inventory.html' when you are logged in.")

# טסט שמרפרש לאחר כניסה למערכת
@allure.feature("login")
def test_refresh_page(page: Page,login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()
    page.reload(wait_until="load")
    login_page.validate_url(configs.products_url)

# כניסה למערכת עם משתמש נעול
@allure.feature("login")
def test_login_with_locked_user(page: Page,login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.locked_out_user)
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()
    login_page.validate_error_message("Sorry, this user has been locked out.")

# כניסה למערכת עם סיסמא שגויה
@allure.feature("login")
def test_login_with_wrong_password(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.fill_password_field("wrong password")
    login_page.click_login_button()
    login_page.validate_error_message("Username and password do not match any user in this service")

# טסט שבודק האם יש הבחנה בין אותיות גדולות לקטנות בשם המשתמש
@allure.feature("login")
def test_case_sensitivity(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user.upper())
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()
    login_page.validate_error_message("Username and password do not match any user in this service")

# טסט שבודק האם ניתן להיכנס למערכת לאחר נסיון כושל
@allure.feature("login")
def test_login_after_failed_attempt(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.click_login_button()
    login_page.fill_username_field(configs.standard_user)
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()
    login_page.validate_url(configs.products_url)