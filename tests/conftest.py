import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture
def checkout_step_one_page(page: Page):
    return CheckoutStepOnePage(page)

@pytest.fixture
def checkout_step_two_page(page: Page):
    return CheckoutStepTwoPage(page)

@pytest.fixture
def checkout_coplete_page(page: Page):
    return CheckoutCompletePage(page)