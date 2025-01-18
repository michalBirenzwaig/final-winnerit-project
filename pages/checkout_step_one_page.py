from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from faker import Faker
import allure

class CheckoutStepOnePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__first_name_field=page.locator('[data-test="firstName"]')
        self.__last_name_field=page.locator('[data-test="lastName"]')
        self.__zip_field=page.locator('[data-test="postalCode"]')
        self.__continue_button=page.get_by_role('button',name='continue')


    def fill_details_with_faker(self):
        with allure.step("Filling in first name, last name, and zip code using the Faker library"):
            fake = Faker()
            self.__first_name_field.fill(fake.first_name())
            self.__last_name_field.fill(fake.last_name())
            self.__zip_field.fill(fake.zipcode())

    def click_continue(self):
        with allure.step("Click on continue button"):
            self.__continue_button.click()