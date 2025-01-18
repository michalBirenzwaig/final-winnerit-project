from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.__items_in_cart = page.locator(".cart_item")
        self.__item_name=page.locator('[data-test="inventory-item-name"]')
        self.__item_price=page.locator('[data-test="inventory-item-price"]')
        self.__open_menu_button=page.get_by_role("button", name="Open Menu")
        self.__reset_button=page.locator('#reset_sidebar_link')
        self.__logout_button=page.locator('[data-test="logout-sidebar-link"]')
        self.__sort_box=page.locator('[data-test="product-sort-container"]')
        self.__item_description=page.locator('[data-test="inventory-item-description"]')
        self.__back_to_products_link=page.locator('#back-to-products')

    def add_to_chart_by_product_name(self,product:str):
        with allure.step(f"Adds to the cart: {product}"):
            self.__page.locator(f"[data-test=\"add-to-cart-{product.replace(" ", "-").lower()}\"]").click()

    def remove_from_chart_by_product_name(self, product: str):
        with allure.step(f"Remove from the cart: {product}"):
            self.__page.locator(f"[data-test=\"remove-{product.replace(" ", "-").lower()}\"]").click()

    def click_cart(self):
        with allure.step("Click on cart"):
            self.__shopping_cart_link.click()

    def count_items_in_cart(self):
        with allure.step("Items in cart"):
            items_in_cart= self.__items_in_cart.count()
            allure.attach(f"Returns the number of items in the cart: {items_in_cart}", name="items_in_cart",
                          attachment_type=allure.attachment_type.TEXT)
            return items_in_cart

    def get_list_products_names_in_cart(self):
        return [self.__item_name.nth(i).inner_text() for i in range(self.__item_name.count())]

    def open_menu(self):
        self.__open_menu_button.click()

    def click_reset_button(self):
        self.open_menu()
        self.__reset_button.click()

    def click_logout_button(self):
        self.open_menu()
        self.__logout_button.click()

    def sort_by_price_low_to_high(self):
        self.__sort_box.select_option("lohi")

    def getting_price_as_float(self,price:str):
        return float(price.replace("$", ""))

    def get_products_prices_in_page(self):
        list_prices=[self.__item_price.nth(i).inner_text() for i in range(self.__item_price.count())]
        return [self.getting_price_as_float(price) for price in list_prices]

    def get_product_price_by_product_name(self,product:str):
        product_item = self.__page.locator('[data-test="inventory-item-description"]', has_text=product)
        price=product_item.locator('[data-test="inventory-item-price"]').inner_text()
        return self.getting_price_as_float(price)

    def get_product_name(self):
        return self.__item_name.inner_text()

    def gat_all_items(self):
        return self.__item_name

    def click_back_to_products(self):
        self.__back_to_products_link.click()