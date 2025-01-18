from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure

class CheckoutStepTwoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__subtotal_label = page.locator('[data-test="subtotal-label"]')
        self.__finish_button=page.get_by_role('button',name='finish')

    def get_subtotal(self):
        with allure.step("Get subtotal value"):
            subtotal=float(self.__subtotal_label.inner_text().replace("Item total: $", ""))
            allure.attach(f"Returned subtotal value: ${subtotal}", name="Subtotal",
                      attachment_type=allure.attachment_type.TEXT)
        return subtotal

    def click_finish(self):
        with allure.step("Click on finish button"):
            self.__finish_button.click()
