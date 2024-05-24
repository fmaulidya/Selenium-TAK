import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.loginData import loginData, loginPage
import loginFailed

class DemoWebShopTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_a_login_success(self):
        browser = self.browser
        browser.get(loginData.url_login)
        self.assertIn(loginData.title, self.browser.title)
        browser.find_element(By.ID, loginPage.email).send_keys(loginData.email_valid)
        browser.find_element(By.ID, loginPage.psw).send_keys(loginData.psw_valid)
        browser.find_element(By.XPATH, loginPage.login_btn).click()
        url = browser.current_url
        self.assertEqual(url, loginData.url)
        browser.quit()

    def test_b_login_failed_invldEmail(self):
        loginFailed.test_baseLoginFailed(self,loginData.email_invalid,loginData.psw_valid,loginData.msg_error_login)

    def test_c_login_failed_invldPass(self):
        loginFailed.test_baseLoginFailed(self,loginData.email_valid,loginData.psw_invalid,loginData.msg_error_login)

    def test_d_login_failed_invldBoth(self):
        loginFailed.test_baseLoginFailed(self,loginData.email_invalid,loginData.psw_invalid,loginData.msg_error_login)

if __name__ == '__main__':
    unittest.main()