import math


def square(side):
    """
    Вычисляет площадь квадрата.
    Если side не целое число, округляет результат вверх.
    """
    area = side * side
    # Округляем вверх, если side не целое число
    if isinstance(side, float) and not side.is_integer():
        return math.ceil(area)
    return area


# Пример использования
print(square(5))     # 25
print(square(3.2))   # 11 (3.2 * 3.2 = 10.24, округляем до 11)
