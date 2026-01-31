from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_calculator_with_delay():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        calculator_page = CalculatorPage(driver)

        calculator_page.open()
        calculator_page.set_delay(45)

        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_operator('=')

        result = calculator_page.get_result()
        assert result == '15', f"Expected result '15', but got '{result}'"
        print(f"Test passed! Result: {result}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator_with_delay()
