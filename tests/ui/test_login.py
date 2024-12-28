from playwright.sync_api import sync_playwright,Page, expect

def test_successful_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("secret_sauce")
        page.get_by_role('button',name='Login').click()
        expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

def test_password_missing():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        page.locator('#user-name').fill("standard_user")
        page.get_by_role('button',name='Login').click()
        expect(page.locator("[data-test='error']")).to_contain_text("Password is required")
