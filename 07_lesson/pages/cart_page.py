from selenium.webdriver.common.by import By


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        """Начать оформление заказа."""
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
