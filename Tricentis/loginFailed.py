import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.loginData import loginPage, loginData

def test_baseLoginFailed(self,userinput,passinput,message):
    browser = self.browser
    browser.get(loginData.url_login)
    self.assertIn(loginData.title, self.browser.title)
    browser.find_element(By.ID, loginPage.email).send_keys(userinput)
    browser.find_element(By.ID, loginPage.psw).send_keys(passinput)
    browser.find_element(By.XPATH, loginPage.login_btn).click()
    error_msg = browser.find_element(By.XPATH, loginPage.err_msg).text
    self.assertIn(message, error_msg)
    browser.quit()