from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
 
 
class CalculatorPage: 
    """Page Object для страницы калькулятора.""" 
 
    def __init__(self, driver): 
        self.driver = driver 
        self.wait = WebDriverWait(driver, 50) 
 
    def open(self): 
        """Открыть страницу калькулятора.""" 
        self.driver.get( 
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html" 
        ) 
 
    def set_delay(self, delay_value): 
        """Установить значение задержки.""" 
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay") 
        delay_field.clear() 
        delay_field.send_keys(str(delay_value)) 
 
    def click_button(self, button_text): 
        """Нажать кнопку с указанным текстом.""" 
        button = self.driver.find_element( 
            By.XPATH, f"//span[text()='{button_text}']" 
        ) 
        button.click() 
 
    def click_operator(self, operator): 
        """Нажать оператор.""" 
        if operator == '=': 
            button = self.driver.find_element( 
                By.CSS_SELECTOR, ".operator[onclick*='equals']" 
            ) 
            button.click() 
        else: 
            # Если не оператор, используем обычную кнопку 
            self.click_button(operator) 
 
    def get_result(self): 
        """Получить результат вычислений.""" 
        result_field = self.driver.find_element(By.CSS_SELECTOR, ".screen") 
        # Ждем пока результат не станет отличным от пустого или '0' 
        self.wait.until( 
            lambda driver: result_field.text not in ['', '0'] 
        ) 
        return result_field.text 
