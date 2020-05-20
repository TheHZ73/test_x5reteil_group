from selenium.webdriver.common.by import By
from config.work_config import Config
import time


class MainGooglePage:
    _button_enter = [By.ID, "gb_70"]
    _email_input = [By.ID, "identifierId"]
    _password_input = [By.XPATH, "//input[@type='password']"]
    _next_button = [By.ID, "identifierNext"]
    _next_button_password = [By.ID, "passwordNext"]
    _mail_button = [By.XPATH, "//a[text()='Почта']"]

    def __init__(self, driver, path_before_config):
        self.file_config = Config(path_before_config)
        self._delay = self.file_config.get("wait_in_second")
        self._driver = driver

    def click_enter_button(self):
        self._driver.find_element(*self._button_enter).click()

    def click_next_button(self):
        self._driver.find_element(*self._next_button).click()

    def click_next_button_password(self):
        self._driver.find_element(*self._next_button_password).click()

    def edit_email_input(self):
        input_text = self.file_config.get("email")
        self._driver.find_element(*self._email_input).send_keys(input_text)

    def edit_password_input(self):
        input_text = self.file_config.get("password")
        time.sleep(5) # загрузка скрытого поля пароля, не стал придумывать для него ожидние
        self._driver.find_element(*self._password_input).send_keys(input_text)

    def click_mail_button(self):
        self._driver.find_element(*self._mail_button).click()
