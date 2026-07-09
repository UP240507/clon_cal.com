from pages.signup_page import SignupPage

def test_signup_email_form_appears(driver):
    page = SignupPage(driver)
    page.load()
    page.open_email_form()
    assert page.find_element(page.USERNAME_INPUT).is_displayed()
    assert page.find_element(page.EMAIL_INPUT).is_displayed()
    assert page.find_element(page.PASSWORD_INPUT).is_displayed()

def test_signup_valid_data_blocked_by_captcha(driver):
    # Caso valido: datos bien formados (email con formato correcto), pero
    # el boton sigue deshabilitado porque el captcha de Turnstile no se
    # ha resuelto. Confirma que el gate aplica incluso a datos correctos.
    page = SignupPage(driver)
    page.load()
    page.open_email_form()
    page.fill_signup_form("usuario_valido", "valido@test.com", "PasswordSegura123")
    assert page.is_email_valid() is True
    assert page.is_submit_enabled() is False

def test_signup_invalid_email_rejected(driver):
    # Caso de error: el navegador rechaza el formato de correo en tiempo
    # real (Constraint Validation API), antes de siquiera tocar el submit.
    page = SignupPage(driver)
    page.load()
    page.open_email_form()
    page.fill_signup_form("us", "sin_arroba.com", "corta")
    assert page.is_email_valid() is False
    assert page.is_submit_enabled() is False

def test_signup_long_username_frontera(driver):
    # Caso de frontera: el campo username no declara maxlength, asi que
    # se verifica que acepta un valor largo completo sin truncarlo.
    page = SignupPage(driver)
    page.load()
    page.open_email_form()
    long_username = "nombre_de_usuario_muy_largo_1234567890"
    page.fill_signup_form(long_username, "frontera@test.com", "P4ssword!")
    assert page.get_username_value() == long_username
    assert page.is_submit_enabled() is False
