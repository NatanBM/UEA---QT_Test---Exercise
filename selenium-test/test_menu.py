from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

import time

class LoginTest(unittest.TestCase):
    
    browser = webdriver.Chrome()
    browser.maximize_window()
    
    def setUp(self):
        self.browser.get('https://www.saucedemo.com/')    
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
    
    def test_ButtonAllItems_CT01(self):
        button_cart = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)
        button_menu = self.browser.find_element(By.ID,'react-burger-menu-btn').click()
        time.sleep(2)
        button_allItems = self.browser.find_element(By.ID,'inventory_sidebar_link').click()
        time.sleep(2)
        label_products = self.browser.find_element(By.CLASS_NAME, 'title').text
        self.assertEqual('Products', label_products)
        time.sleep(3)
    
    def test_ButtonAbout_CT02(self):
        Button_menu = self.browser.find_element(By.ID,'react-burger-menu-btn').click()
        time.sleep(2)
        button_about = self.browser.find_element(By.ID,'about_sidebar_link').click()
        time.sleep(2)
        button_products = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/p').text
        self.assertEqual('The world relies on your code. Test on thousands of different device, browser, and OS configurations–anywhere, any time.', button_products) 
        time.sleep(3)      
    
    def test_ButtonLogout_CT03(self):
        button_menu = self.browser.find_element(By.ID,'react-burger-menu-btn').click()
        time.sleep(2)
        button_about = self.browser.find_element(By.ID,'logout_sidebar_link').click()
        time.sleep(2)
        button_login = self.browser.find_element(By.ID, 'login-button').text
        self.assertEqual('', button_login)        
        time.sleep(2)       
    
    def test_ButtonResetAppState_CT04(self):
        button_addBikeLight = self.browser.find_element(By.ID,'add-to-cart-sauce-labs-bike-light').click()
        time.sleep(2)
        button_menu = self.browser.find_element(By.ID,'react-burger-menu-btn').click()
        time.sleep(2)
        button_reset = self.browser.find_element(By.ID,'reset_sidebar_link').click()
        time.sleep(2)
        label_checkButtonCart = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_container').text
        self.assertEqual('', label_checkButtonCart)        
        label_checkButtonAdd = self.browser.find_element(By.ID, 'remove-sauce-labs-bike-light').text
        self.assertEqual('Add to cart', label_checkButtonAdd)
        time.sleep(3)
    
if __name__ == '__main__':
        unittest.main()      

