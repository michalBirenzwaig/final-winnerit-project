from itertools import count

from playwright.sync_api import sync_playwright,Page, expect

def test_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        product1 = "Sauce Labs Bolt T-Shirt"
        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("secret_sauce")
        page.get_by_role('button',name='Login').click()
        products_list = page.locator('[data-test="inventory-item-name"]')
        products_count = products_list.count()
        #for i in range(products_count):
         #   product_text = products_list.nth(i).inner_text()
          #  print(product_text)
          #  parent_element = products_list.nth(i).locator('.. >> [data-test="inventory-item-description"]')
           # price_text_list=parent_element.locator('[data-test="inventory-item-price"]').inner_text()
           # print(f"price_text_list=")

def test_add_to_cart_and_remove():
    with sync_playwright() as p:
        product1="Sauce Labs Backpack"
        product2="Sauce Labs Fleece Jacket"
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("secret_sauce")
        page.get_by_role('button', name='Login').click()
        page.locator(f"[data-test=\"add-to-cart-{product1.replace(" ", "-").lower()}\"]").click()
        page.locator(f"[data-test=\"add-to-cart-{product2.replace(" ", "-").lower()}\"]").click()
        page.locator('[data-test="shopping-cart-link"]').click()
        assert page.locator(".cart_item").count()==2
        items_in_cart=page.locator('[data-test="inventory-item-name"]')
        count_items=items_in_cart.count()
        cart_texts = [items_in_cart.nth(i).inner_text() for i in range(count_items)]
        print(cart_texts)
        assert product1 in cart_texts
        assert product2 in cart_texts
        page.locator(f"[data-test=\"remove-{product2.replace(" ", "-").lower()}\"]").click()
        assert page.locator(".cart_item").count()==1
        items_in_cart = page.locator('[data-test="inventory-item-name"]')
        count_items = items_in_cart.count()
        cart_texts = [items_in_cart.nth(i).inner_text() for i in range(count_items)]
        print(cart_texts)
        assert product1 in cart_texts


def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("secret_sauce")
        page.get_by_role('button',name='Login').click()
        page.get_by_role("button", name="Open Menu").click()
        page.locator('[data-test="logout-sidebar-link"]').click()
        expect(page).to_have_url('https://www.saucedemo.com/')

def test_sort_by_price():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("secret_sauce")
        page.get_by_role('button',name='Login').click()
        page.locator('[data-test="product-sort-container"]').select_option("lohi")
        products_in_page=page.locator('[data-test="inventory-item-price"]')
        count_items = products_in_page.count()
        price_texts = [products_in_page.nth(i).inner_text() for i in range(count_items)]
        prices = [float(price.replace("$", "")) for price in price_texts]
        for i in range(1, len(prices)):
            assert prices[i - 1] <= prices[i]


