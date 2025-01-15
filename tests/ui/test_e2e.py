import utils.configs as configs
import pytest

@pytest.fixture()
def login_to_app(login_page):
    login_page.navigate_to(configs.base_url)
    login_page.fill_username_field(configs.standard_user)
    login_page.fill_password_field(configs.correct_password)
    login_page.click_login_button()

# טסט שמוסיף מוצרים לסל ובודק את הסכום לתשלום הסופי
def test_order_and_payment(login_to_app,login_page,products_page,cart_page,
                           checkout_step_one_page,checkout_step_two_page,checkout_coplete_page):
    sum=0
    sum+=products_page.get_product_price_by_product_name(configs.product_Jacket)
    sum+=products_page.get_product_price_by_product_name(configs.product_Backpack)
    products_page.add_to_chart_by_product_name(configs.product_Jacket)
    products_page.add_to_chart_by_product_name(configs.product_Backpack)
    products_page.click_cart()
    cart_page.validate_url(configs.cart_url)
    cart_page.click_checkout_button()
    checkout_step_one_page.validate_url(configs.checkout_step_one_url)
    checkout_step_one_page.fill_details_with_faker()
    checkout_step_one_page.click_continue()
    checkout_step_two_page.validate_url(configs.checkout_step_two_url)
    assert checkout_step_two_page.get_subtotal()==sum
    checkout_step_two_page.click_finish()
    checkout_coplete_page.validate_url(configs.checkout_complete_url)

# טסט שמוסיף מוצרים לסל ואח"כ מסיר ממנו
def test_add_to_cart_and_remove(login_to_app,login_page,products_page):
    products_page.add_to_chart_by_product_name(configs.product_Backpack)
    products_page.add_to_chart_by_product_name(configs.product_Jacket)
    products_page.click_cart()
    assert products_page.count_items_in_cart()==2
    products_in_cart=products_page.get_products_names_in_cart()
    assert configs.product_Backpack in products_in_cart
    assert configs.product_Jacket in products_in_cart
    products_page.remove_from_chart_by_product_name(configs.product_Jacket)
    assert products_page.count_items_in_cart() == 1
    products_in_cart = products_page.get_products_names_in_cart()
    assert configs.product_Backpack in products_in_cart

# לחיצה על logout ובדיקה שחזרנו לעמוד הראשי
def test_logout(login_to_app,login_page,products_page):
    products_page.click_logout_button()
    login_page.validate_url(configs.base_url)

# טסט שבודק מיון מוצרים מהמחיר הנמוך לגבוה
def test_sort_by_price(login_to_app,login_page,products_page):
    products_page.sort_by_price_low_to_high()
    prices_in_page=products_page.get_products_prices_in_page()
    for i in range(1, len(prices_in_page)):
        assert prices_in_page[i - 1] <= prices_in_page[i]

# טסט שלוחץ על כל מוצר ובודק שנפתח עמוד המוצר עם הפרטים הנכונים
def test_link_product(login_to_app,login_page,products_page):
         list_products=products_page.gat_all_items()
         count_items = list_products.count()
         for i in range(count_items):
              product_name=list_products.nth(i).inner_text()
              list_products.nth(i).click()
              product_name_in_details_page=products_page.get_product_name()
              assert product_name==product_name_in_details_page
              products_page.click_back_to_products()

# לחיצה על reset app state ובדיקה שאכן הסל התאפס
def test_reset_app_state(login_to_app,login_page,products_page):
    products_page.add_to_chart_by_product_name(configs.product_Backpack)
    products_page.add_to_chart_by_product_name(configs.product_Jacket)
    products_page.click_reset_button()
    products_page.click_cart()
    assert products_page.count_items_in_cart() == 0
