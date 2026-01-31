from selenium import webdriver 
from pages.login_page import LoginPage 
from pages.main_page import MainPage 
from pages.cart_page import CartPage 
from pages.checkout_page import CheckoutPage 
 
 
def test_saucedemo_shopping(): 
    """Тест интернет-магазина.""" 
    driver = webdriver.Firefox() 
    driver.maximize_window() 
    
    try: 
        login_page = LoginPage(driver) 
        main_page = MainPage(driver) 
        cart_page = CartPage(driver) 
        checkout_page = CheckoutPage(driver) 
        
        # 1. Открыть сайт магазина 
        login_page.open() 
        
        # 2. Авторизоваться 
        login_page.login("standard_user", "secret_sauce") 
        
        # 3. Добавить товары в корзину 
        main_page.add_to_cart("Sauce Labs Backpack") 
        main_page.add_to_cart("Sauce Labs Bolt T-Shirt") 
        main_page.add_to_cart("Sauce Labs Onesie") 
        
        # 4. Перейти в корзину 
        main_page.go_to_cart() 
        
        # 5. Нажать Checkout 
        cart_page.checkout() 
        
        # 6. Заполнить форму 
        checkout_page.fill_checkout_info("John", "Doe", "12345") 
        
        # 7. Получить итоговую стоимость 
        total_price = checkout_page.get_total_price() 
        
        # 8. Проверить сумму 
        assert total_price == "58.29", f"Expected \$58.29, got \${total_price}" 
        print(f"Test passed! Total price: \${total_price}") 
    
    finally: 
        driver.quit() 
 
 
if __name__ == "__main__": 
    test_saucedemo_shopping() 
