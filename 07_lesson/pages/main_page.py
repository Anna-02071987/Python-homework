from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        xpath = f"//div[text()='{product_name}']"
        xpath += "/ancestor::div[@class='inventory_item']//button"
        add_button = self.driver.find_element(By.XPATH, xpath)
        add_button.click()

    def go_to_cart(self):
        cart_button = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()
