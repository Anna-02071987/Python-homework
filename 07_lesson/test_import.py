# -*- coding: utf-8 -*- 
"""Тестовый файл для проверки импортов Page Object классов""" 
 
print("Проверка импортов Page Object классов...") 
 
try: 
    from pages.calculator_page import CalculatorPage 
    from pages.login_page import LoginPage 
    from pages.main_page import MainPage 
    from pages.cart_page import CartPage 
    from pages.checkout_page import CheckoutPage 
    print("? Все импорты работают корректно") 
except ImportError as e: 
    print(f"? Ошибка импорта: {e}") 
