import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.loginData import CheckOutData,CheckOutPage,loginData,loginPage, BillingData, BillingPage

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
        browser.find_element(By.ID, BillingPage.First_Name).send_keys(BillingData.Bill_First_Name)
        browser.find_element(By.ID, BillingPage.Last_Name).send_keys(BillingData.Bill_Last_Name)
        browser.find_element(By.ID, BillingPage.Email).send_keys(CheckOutData.snd_email_valid)
        browser.find_element(By.ID, BillingPage.Company).send_keys(BillingData.Bill_Company)
        browser.find_element(By.ID, BillingPage.Country).send_keys(BillingData.Bill_Country)
        browser.find_element(By.ID, BillingPage.State).send_keys(BillingData.Bill_State)
        browser.find_element(By.ID, BillingPage.City).send_keys(BillingData.Bill_City)
        browser.find_element(By.ID, BillingPage.Address1).send_keys(BillingData.Bill_Address1)
        browser.find_element(By.ID, BillingPage.Address2).send_keys(BillingData.Bill_Address2)
        browser.find_element(By.ID, BillingPage.ZipCode).send_keys(BillingData.Bill_ZipCode)
        browser.find_element(By.ID, BillingPage.Ph_No).send_keys(BillingData.Bill_Ph_No)
        browser.find_element(By.ID, BillingPage.Fax_no).send_keys(BillingData.Bill_Fax_no)
        browser.find_element(By.XPATH, BillingPage.cnt_btn).click()
        browser.find_element(By.XPATH, BillingPage.COD_rad).click()
        browser.find_element(By.XPATH, BillingPage.cnt_btn_pm).click()
        browser.find_element(By.XPATH, BillingPage.cnt_btn_pi).click()
        browser.find_element(By.XPATH, BillingPage.confirm_btn).click()
        browser.implicitly_wait(100)
        url = browser.current_url
        self.assertEqual(url, CheckOutData.url_complete)
        browser.find_element(By.XPATH, CheckOutPage.ctn_btn).click()
        url = browser.current_url
        self.assertEqual(url, CheckOutData.url)
        browser.quit()
        

if __name__ == '__main__':
    unittest.main()