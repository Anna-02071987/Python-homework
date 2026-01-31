from selenium.webdriver.common.by import By 
 
class LoginPage: 
    """Page Object для страницы авторизации.""" 
 
    def __init__(self, driver): 
        self.driver = driver 
 
    def open(self): 
        """Открыть страницу авторизации.""" 
        self.driver.get("https://www.saucedemo.com/") 
 
    def login(self, username, password): 
        """Выполнить авторизацию.""" 
        username_field = self.driver.find_element(By.ID, "user-name") 
        password_field = self.driver.find_element(By.ID, "password") 
        login_button = self.driver.find_element(By.ID, "login-button") 
 
        username_field.send_keys(username) 
        password_field.send_keys(password) 
        login_button.click() 
