from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver= driver

    link_login_xpath= "//span[normalize-space()='Log In']"
    link_contactus_linktext = "Contact Us"
    text_email_xpath= "//li[normalize-space()='support@asteriskt.com']"

    def clickContactUs(self):
        self.driver.find_element(By.LINK_TEXT, self.link_contactus_linktext)

    def clickLogIn(self):
        self.driver.find_element(By.XPATH, self.link_login_xpath).click()

    def confirmHomePage(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_email_xpath).text
        except:
            None
