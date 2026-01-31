# ============================================================================
# Homework for Lesson 5: Selenium WebDriver Basics
# Created: 2026-01-16
# ============================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

# Упражнение 3. Поле ввода
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Открыть браузер FireFox и перейти на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    # Найти поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Ввести в поле текст Sky
    input_field.send_keys("Sky")
    time.sleep(2)

    # Очистить это поле
    input_field.clear()
    time.sleep(2)

    # Ввести в поле текст Pro
    input_field.send_keys("Pro")
    time.sleep(2)

    print("Упражнение 3 выполнено успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
