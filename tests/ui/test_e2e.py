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