from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config.work_config import Config


class MailPage:
    _first_element_in_mail = (By.XPATH, '//table[@role="grid"]//tbody//tr[1]')

    def __init__(self, driver, path_before_config, text_letter):
        self.file_config = Config(path_before_config)
        self._delay = int(self.file_config.get("wait_in_second"))
        self._driver = driver
        self.text_of_letter = text_letter
        self.wait_download_page()

    def wait_download_page(self):
        WebDriverWait(self._driver, self._delay).until(
            expected_conditions.presence_of_element_located(self._first_element_in_mail))

    def checking_that_the_email_has_arrived(self):
        try:
            xpath_element = '//span[text()="{}"]'.format(self.text_of_letter)
            mail_text_element = [By.XPATH, xpath_element]
            element = self._driver.find_element(*mail_text_element)
        except NoSuchElementException:
            return False
        return True
