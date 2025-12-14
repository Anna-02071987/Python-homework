def is_year_leap(year):
    """
    Проверяет, является ли год високосным.
    """
    return year % 4 == 0


# Вызываем функцию с любым годом
year = 2024
result = is_year_leap(year)
print(f"год {year}: {result}")
