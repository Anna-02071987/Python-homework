# ============================================================================
# Homework for Lesson 5: Selenium WebDriver Basics
# Created: 2026-01-16
# ============================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Упражнение 1. Клик по кнопке с CSS-классом
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открыть браузер Google Chrome и перейти на страницу
    driver.get("http://uitestingplayground.com/classattr")
    time.sleep(2)

    # Найти синюю кнопку по классу
    blue_button = driver.find_element(
        By.XPATH, "//button[contains(@class, 'btn-primary')]"
    )
    blue_button.click()
    time.sleep(3)

    print("Упражнение 1 выполнено успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
