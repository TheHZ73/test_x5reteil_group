from common import BaseTest
from pages.main_google_page import MainGooglePage
from pages.mail_page import MailPage
from config.work_config import Config
from api_methods.api_methods import UsingApi
import allure


class TestClass(BaseTest):
    @allure.testcase('Test sending email')
    def test_send_mail_in_gmail(self, driver_transfer, path_before_config):
        with allure.step('Step 1: send mail from api'):
            file_config = Config(path_before_config)
            api_methods = UsingApi(path_before_config)
            api_methods.send_email_api_method()
        with allure.step('Step 2: go to google homepage'):
            url = file_config.get("url")
            driver_transfer.instance.get(url)
        with allure.step('Step 3: click to enter button'):
            main_google_page = MainGooglePage(driver_transfer.instance, path_before_config)
            main_google_page.click_enter_button()
        with allure.step('Step 4: login in account'):
            main_google_page.edit_email_input()
            main_google_page.click_next_button()
            main_google_page.edit_password_input()
            main_google_page.click_next_button_password()
        with allure.step('Step 5: click mail button'):
            main_google_page.click_mail_button()
        with allure.step('Step 6: checking that the email has arrived'):
            mail_page = MailPage(driver_transfer.instance, path_before_config, api_methods.text_mail)
            assert mail_page.checking_that_the_email_has_arrived()


