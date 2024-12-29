from itertools import count
from time import sleep

from playwright.sync_api import sync_playwright,Page, expect

# טסט שמוסיף מוצרים לסל ובודק את הסכום לתשלום הסופי
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

# טסט שמוסיף מוצרים לסל ואח"כ מסיר ממנו
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

# לחיצה על logout ובדיקה שחזרנו לעמוד הראשי
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

# טסט שבודק מיון מוצרים מהמחיר הנמוך לגבוה
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

# טסט שלוחץ על כל מוצר ובודק שנפתח עמוד המוצר עם הפרטים הנכונים
def test_link_product():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("secret_sauce")
        page.get_by_role('button',name='Login').click()
        list_products=page.locator('[data-test="inventory-item-name"]')
        count_items = list_products.count()
        for i in range(count_items):
            product_name=list_products.nth(i).inner_text()
            list_products.nth(i).click()
            product_name_in_details_page=page.locator('[data-test="inventory-item-name"]').inner_text()
            assert product_name==product_name_in_details_page
            page.locator('#back-to-products').click()

# לחיצה על reset app state ובדיקה שאכן הסל התאפס
def test_reset_app_state():
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
        page.get_by_role("button", name="Open Menu").click()
        page.locator('#reset_sidebar_link').click()
        page.locator('[data-test="shopping-cart-link"]').click()
        assert page.locator(".cart_item").count() == 0
