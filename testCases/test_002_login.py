from utilities import XLutils
from utilities.customerlogger import LogGen
from pageObjects.loginPage import LoginPage
from pageObjects.homepage import HomePage
from pageObjects.dashboardPage import DashboardPage
import os
import pytest

class TestLogin:
    excel_filepath= os.path.abspath(os.curdir)+"//testData//login_test_data.xlsx"
    logger= LogGen.loggen()

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("Test Started")
        self.driver= setup
        self.driver.get("https://merolagani.com/")
        self.driver.implicitly_wait(10)
        self.logger.info("Opened MeroLagani.com")
        self.homepage= HomePage(self.driver)
        self.homepage.clickLogIn()
        self.logger.info("Clicked on Login")
        self.driver.implicitly_wait(10)
        self.dashboard = DashboardPage(self.driver)
        self.loginpage= LoginPage(self.driver)
        if self.loginpage.confirmLoginPage()=='Log In':
            self.logger.info("Login Page Opening Passed")
            assert True
        else:
            self.logger.info("Login Page Opening Failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//loginpage_test_fail.png")
            self.driver.close()
            assert False
        #reading the data fro excel file
        self.maxrows= XLutils.getRowCount(self.excel_filepath, "login_data")
        self.logger.info("Login Attempts Started")
        for r in range(2, self.maxrows+1):
            self.emailid= XLutils.readData(self.excel_filepath, "login_data", r, 2)
            self.passid = XLutils.readData(self.excel_filepath, "login_data", r, 3)
            #setting the data in the email and password box
            self.loginpage.setEmail(self.emailid)
            self.loginpage.setPassword(self.passid)
            self.loginpage.clickLoginButton()
            self.driver.implicitly_wait(10)
            if self.dashboard.confirmDashboardPage()==True:
                self.dashboard.logoutDashboardPage()
            else:
                self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//login_test_fail.png")
        self.driver.close()
        self.logger.info("Test Completed")






