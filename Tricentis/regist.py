import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.registData import registData, registPage

def test_registFailed(self,userinput,passinput,message):
    browser = self.browser
    browser.get(registData.url_regist)
    self.assertIn(loginData.title, self.browser.title)
    browser.find_element(By.NAME, loginPage.user).send_keys(userinput)
    browser.find_element(By.NAME, loginPage.psw).send_keys(passinput)
    browser.find_element(By.ID, loginPage.login_btn).click()
    error_msg = browser.find_element(By.CSS_SELECTOR, loginPage.err_msg).text
    self.assertIn(message, error_msg)
    browser.quit()

if __name__ == '__main__':
    unittest.main()