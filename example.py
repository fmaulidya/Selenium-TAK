from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://demowebshop.tricentis.com/register')
browser.find_element(By.ID,'gender-female').click()