from selenium.webdriver.common.by import By
from .base_page import BasePage

class AuthPage(BasePage):
    # Localizadores (Adaptados a los selectores comunes de una app genérica/cal.com)
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-red-500, [role='alert']")

    def load(self):
        self.driver.get("https://app.cal.com/auth/login")

    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.SUBMIT_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text