from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_saucedemo_shopping():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        main_page.add_to_cart("Sauce Labs Backpack")
        main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        main_page.add_to_cart("Sauce Labs Onesie")

        main_page.go_to_cart()
        cart_page.checkout()
        checkout_page.fill_checkout_info("John", "Doe", "12345")

        total_price = checkout_page.get_total_price()
        expected = "58.29"
        message = f"Expected ${expected}, got ${total_price}"
        assert total_price == expected, message
        print(f"Test passed! Total price: ${total_price}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_saucedemo_shopping()
