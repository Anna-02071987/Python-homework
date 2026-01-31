# ============================================================================
# Homework for Lesson 5: Selenium WebDriver Basics
# Created: 2026-01-16
# ============================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

# Упражнение 4. Форма авторизации
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Открыть браузер FireFox и перейти на страницу
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    # Найти поле username и ввести значение tomsmith
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Найти поле password и ввести значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    time.sleep(2)

    # Найти кнопку Login и нажать её
    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    login_button.click()
    time.sleep(2)

    # Найти зелёную плашку с сообщением об успехе
    success_message = driver.find_element(By.ID, "flash")

    # Вывести текст с зелёной плашки в консоль
    print("Текст с зелёной плашки:")
    print(success_message.text)

    print("\nУпражнение 4 выполнено успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
