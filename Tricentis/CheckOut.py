import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.loginData import CheckOutData,CheckOutPage,loginData,loginPage

class DemoWebShopTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_a_CheckOutAsGuest(self):
        browser = self.browser
        browser.get(CheckOutData.url)
        self.assertIn(loginData.title, self.browser.title)
        self.assertIn(CheckOutData.title, self.browser.title)
        browser.find_element(By.XPATH, CheckOutPage.add_cart_btn).click()
        browser.find_element(By.XPATH, CheckOutPage.go_to_cart).click()
        url = browser.current_url
        self.assertEqual(url, CheckOutData.url_VGC)
        browser.find_element(By.ID, CheckOutPage.rec_name).send_keys(CheckOutData.rec_name_valid)
        browser.find_element(By.ID, CheckOutPage.rec_email).send_keys(CheckOutData.rec_email_valid)
        browser.find_element(By.ID, CheckOutPage.snd_name).send_keys(CheckOutData.snd_name_valid)
        browser.find_element(By.ID, CheckOutPage.snd_email).send_keys(CheckOutData.snd_email_valid)
        browser.find_element(By.XPATH, CheckOutPage.add_cart_btn2).click()
        browser.find_element(By.XPATH, CheckOutPage.go_to_cart).click()
        browser.implicitly_wait(3)
        url = browser.current_url
        self.assertEqual(url, CheckOutData.url_cart)
        browser.find_element(By.NAME, CheckOutPage.tns).click()
        browser.find_element(By.XPATH, CheckOutPage.co_btn).click()
        browser.implicitly_wait(3)
        browser.find_element(By.XPATH, CheckOutPage.co_guest_btn).click()
        


        #browser.quit()

if __name__ == '__main__':
    unittest.main()