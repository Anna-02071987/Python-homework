from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object для страницы калькулятора."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        """Открыть страницу калькулятора."""
        url = "https://bonigarcia.dev/"
        url += "selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)

    def set_delay(self, delay_value):
        """Установить значение задержки."""
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def click_button(self, button_text):
        """Нажать кнопку с указанным текстом."""
        xpath = f"//span[text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def click_operator(self, operator):
        """Нажать оператор."""
        if operator == '=':
            button = self.driver.find_element(
                By.CSS_SELECTOR, ".operator[onclick*='equals']")
            button.click()
        else:
            self.click_button(operator)

    def get_result(self):
        """Получить результат вычислений."""
        result_field = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        self.wait.until(lambda driver: result_field.text not in ['', '0'])
        return result_field.text
