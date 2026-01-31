from selenium.webdriver.common.by import By 
 
 
class CheckoutPage: 
    """Page Object для страницы оформления заказа.""" 
 
    def __init__(self, driver): 
        self.driver = driver 
 
    def fill_checkout_info(self, first_name, last_name, zip_code): 
        """Заполнить информацию для оформления заказа.""" 
        first_name_field = self.driver.find_element(By.ID, "first-name") 
        last_name_field = self.driver.find_element(By.ID, "last-name") 
        postal_code_field = self.driver.find_element(By.ID, "postal-code") 
        continue_button = self.driver.find_element(By.ID, "continue") 
 
        first_name_field.send_keys(first_name) 
        last_name_field.send_keys(last_name) 
        postal_code_field.send_keys(zip_code) 
        continue_button.click() 
 
    def get_total_price(self): 
        """Получить итоговую стоимость.""" 
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label") 
        total_text = total_element.text 
        # Извлекаем число из строки вида "Total: $58.29" 
        return total_text.split("\$")[1] 
