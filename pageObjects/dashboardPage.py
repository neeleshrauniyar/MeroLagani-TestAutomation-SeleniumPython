from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver= driver

    text_dashboard_xpath= "//span[normalize-space()='Dashboard']"
    dropdown_options_xpath= "//label[@id='ctl00_lblUsername']"
    link_logout_xpath="//ul[@class='dropdown-menu']//a[normalize-space()='Log Out']"

    def confirmDashboardPage(self):
        return self.driver.find_element(By.XPATH, self.text_dashboard_xpath).is_displayed()

    def logoutDashboardPage(self):
        self.driver.find_element(By.XPATH, self.dropdown_options_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

