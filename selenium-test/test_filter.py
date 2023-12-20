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
    
    def test_filtro_A_Z_CT01(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        botao_filterZ_A = self.browser.find_element(By.CLASS_NAME, 'product_sort_container')
        botao_filterZ_A.send_keys('Name (Z to A)')
        botao_filterA_Z = self.browser.find_element(By.CLASS_NAME, 'product_sort_container')
        botao_filterA_Z.send_keys('Name (A to Z)')
        validacaoA_Z = self.browser.find_element(By.CLASS_NAME, 'inventory_item_name').text
        self.assertEqual('Sauce Labs Backpack', validacaoA_Z)
        time.sleep(3)
        
    def test_filtro_Z_A_CT02(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        botao_filterZ_A = self.browser.find_element(By.CLASS_NAME, 'product_sort_container')
        botao_filterZ_A.send_keys('Name (Z to A)')
        time.sleep(2)
        validacaoZ_A = self.browser.find_element(By.CLASS_NAME, 'inventory_item_name').text
        self.assertEqual('Test.allTheThings() T-Shirt (Red)', validacaoZ_A)
        time.sleep(3)
    
    def test_Price_Low_To_High_CT03(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        botao_filterPrice_low_to_High = self.browser.find_element(By.CLASS_NAME, 'product_sort_container')
        botao_filterPrice_low_to_High.send_keys('Price (low to high)')
        time.sleep(2)
        validacaoPriceLow_to_high = self.browser.find_element(By.CLASS_NAME, 'inventory_item_name').text
        self.assertEqual('Sauce Labs Onesie', validacaoPriceLow_to_high)
        time.sleep(3)
    
    def test_Price_Low_To_High_CT04(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        botao_filterPrice_low_to_High = self.browser.find_element(By.CLASS_NAME, 'product_sort_container')
        botao_filterPrice_low_to_High.send_keys('Price (low to high)')
        botao_filterPrice_high_to_low = self.browser.find_element(By.CLASS_NAME, 'product_sort_container')
        botao_filterPrice_high_to_low.send_keys('Price (high to low)')
        time.sleep(2)
        validacaoPricehight_to_low = self.browser.find_element(By.CLASS_NAME, 'inventory_item_name').text
        self.assertEqual('Sauce Labs Fleece Jacket', validacaoPricehight_to_low)
        time.sleep(3)

if __name__ == '__main__':
        unittest.main()      