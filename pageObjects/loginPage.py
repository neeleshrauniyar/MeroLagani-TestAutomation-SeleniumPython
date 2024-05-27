from selenium.webdriver.common.by import By

class LoginPage:
    link_email_xpath= "//input[@id='ctl00_ContentPlaceHolder1_login1_txtEmail']"
    link_password_xpath= "//input[@id='ctl00_ContentPlaceHolder1_login1_txtPassword']"
    btn_login_xpath="//a[@id='ctl00_ContentPlaceHolder1_login1_lbtnLogin']"
    text_login_xpath= "//h3[normalize-space()='Log In']"

    def __init__(self, driver):
        self.driver= driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.link_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.link_password_xpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def confirmLoginPage(self):
        return self.driver.find_element(By.XPATH, self.text_login_xpath).text
