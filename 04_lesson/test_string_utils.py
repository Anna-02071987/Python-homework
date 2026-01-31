from string_utils import StringUtils


class TestStringUtils:
    """Тесты для класса StringUtils"""

    def test_capitalize_positive(self):
        """Позитивный тест: обычная строка"""
        utils = StringUtils()
        result = utils.capitalize("skypro")
        assert result == "Skypro", f"Ожидалось 'Skypro', получено '{result}'"

    def test_capitalize_empty_string(self):
        """Негативный тест: пустая строка"""
        utils = StringUtils()
        result = utils.capitalize("")
        assert result == "", f"Ожидалось пустая строка, получено '{result}'"

    # Тесты для функции trim()
    def test_trim_with_spaces(self):
        """Позитивный тест: строка с пробелами в начале"""
        utils = StringUtils()
        result = utils.trim("   skypro")
        assert result == "skypro", f"Ожидалось 'skypro', получено '{result}'"

    def test_trim_without_spaces(self):
        """Негативный тест: строка без пробелов в начале"""
        utils = StringUtils()
        result = utils.trim("skypro")
        assert result == "skypro", f"Ожидалось 'skypro', получено '{result}'"

    def test_trim_empty_string(self):
        """Негативный тест: пустая строка"""
        utils = StringUtils()
        result = utils.trim("")
        assert result == "", f"Ожидалось пустая строка, получено '{result}'"

    # Тесты для функции contains()
    def test_contains_positive(self):
        """Позитивный тест: символ присутствует"""
        utils = StringUtils()
        result = utils.contains("SkyPro", "S")
        assert result is True, f"Ожидалось True, получено {result}"

    def test_contains_negative(self):
        """Негативный тест: символ отсутствует"""
        utils = StringUtils()
        result = utils.contains("SkyPro", "U")
        assert result is False, f"Ожидалось False, получено {result}"

    def test_contains_empty_string(self):
        """Негативный тест: пустая строка"""
        utils = StringUtils()
        result = utils.contains("", "a")
        assert result is False, f"Ожидалось False, получено {result}"

    # Тесты для функции delete_symbol()
    def test_delete_symbol_positive(self):
        """Позитивный тест: удаление одного символа"""
        utils = StringUtils()
        result = utils.delete_symbol("SkyPro", "k")
        assert result == "SyPro", f"Ожидалось 'SyPro', получено '{result}'"

    def test_delete_symbol_substring(self):
        """Позитивный тест: удаление подстроки"""
        utils = StringUtils()
        result = utils.delete_symbol("SkyPro", "Pro")
        assert result == "Sky", f"Ожидалось 'Sky', получено '{result}'"

    def test_delete_symbol_not_found(self):
        """Негативный тест: символ не найден"""
        utils = StringUtils()
        result = utils.delete_symbol("SkyPro", "X")
        assert result == "SkyPro", f"Ожидалось 'SkyPro', получено '{result}'"
