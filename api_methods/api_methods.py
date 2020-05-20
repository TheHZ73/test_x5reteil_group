from datetime import datetime
from config.work_config import Config
import smtplib


class UsingApi:
    def __init__(self, path_before_config):
        self.file_config = Config(path_before_config)
        self.text_mail = 'Text_mail_for_check_{}'.format(datetime.now().strftime('%d%m%Y%H%M%S'))

    def send_email_api_method(self):
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        name_email = self.file_config.get("email")
        password_mail = self.file_config.get("password")
        smtp_obj.login(name_email, password_mail)
        smtp_obj.sendmail(name_email, name_email, self.text_mail)
        smtp_obj.quit()