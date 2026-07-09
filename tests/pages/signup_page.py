from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignupPage(BasePage):
    # Localizadores verificados contra https://app.cal.com/signup (data-testid reales)
    CONTINUE_WITH_EMAIL_BUTTON = (By.CSS_SELECTOR, "[data-testid='continue-with-email-button']")
    USERNAME_INPUT = (By.NAME, "username")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid='signup-submit-button']")

    def load(self):
        self.driver.get("https://app.cal.com/signup")

    def open_email_form(self):
        # La pantalla inicial solo ofrece Google/Microsoft/SAML/email;
        # hay que abrir explícitamente el formulario de correo.
        self.click_element(self.CONTINUE_WITH_EMAIL_BUTTON)

    def fill_signup_form(self, username, email, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)

    def is_submit_enabled(self):
        return self.find_element(self.SUBMIT_BUTTON).is_enabled()

    def is_email_valid(self):
        # El input de email es type="email": el navegador valida el formato
        # en tiempo real via la Constraint Validation API, sin necesidad
        # de enviar el formulario.
        email_el = self.find_element(self.EMAIL_INPUT)
        return self.driver.execute_script("return arguments[0].checkValidity();", email_el)

    def get_username_value(self):
        return self.find_element(self.USERNAME_INPUT).get_attribute("value")
