import os.path
from pageObjects.homepage import HomePage
from utilities.customerlogger import LogGen
import pytest

class TestHomePage:
    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_homepage(self, setup):
        self.driver=setup
        self.driver.get("https://merolagani.com/")
        self.logger.info("Opened website")
        self.homepage= HomePage(self.driver)
        self.homepage.clickContactUs()
        self.conf_message= self.homepage.confirmHomePage()
        if self.conf_message=='support@asteriskt.com':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//test_fail.png")
            self.driver.close()
            assert False
