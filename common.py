import pytest
from config.work_config import Config


class BaseTest(object):
    @pytest.fixture(scope="class", autouse=True)
    def setup_teardown(self, request, driver_transfer, path_before_config):
        driver_transfer.start()
        file_config = Config(path_before_config)
        delay = file_config.get("wait_in_second")
        driver_transfer.instance.implicitly_wait(delay)
        driver_transfer.instance.maximize_window()

        request.addfinalizer(driver_transfer.stop)
