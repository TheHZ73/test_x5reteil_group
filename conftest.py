from selenium import webdriver
import pytest


path_config = "config\config.conf"


class DriverManager(object):
    def __init__(self):
        self._instance = None

    def start(self):
        self._instance = webdriver.Chrome()
        return self._instance

    @property
    def instance(self):
        if not self._instance:
            self.start()
        return self._instance

    def stop(self):
        if self._instance:
            self._instance.close()


@pytest.fixture(scope="module")
def driver_transfer():
    return DriverManager()


@pytest.fixture(scope="module")
def path_before_config():
    return path_config





