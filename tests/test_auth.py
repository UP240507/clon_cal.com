import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage

def test_login_empty_fields(driver):
    page = AuthPage(driver)
    page.load()
    page.click_element(page.SUBMIT_BUTTON)
    assert "login" in driver.current_url

@pytest.mark.parametrize("email, password", [
    ("usuario_invalido@test.com", "12345"),
    ("sin_arroba.com", "password123"),
    ("test@cal.com", "corta")
])
def test_login_invalid_credentials(driver, email, password):
    page = AuthPage(driver)
    page.load()
    page.login(email, password)
    
    wait = WebDriverWait(driver, 5)
    is_still_on_login = wait.until(EC.url_contains("login"))
    
    assert is_still_on_login == True

# Prueba 5: Caso válido de carga
def test_login_page_loads_correctly(driver):
    page = AuthPage(driver)
    page.load()
    assert "Cal.com" in driver.title