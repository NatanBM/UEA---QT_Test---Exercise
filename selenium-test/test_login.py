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
    
    def test_login_de_sucesso_CT01(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        label_titulo = self.browser.find_element(By.CLASS_NAME, 'title').text
        self.assertEqual('Products', label_titulo)
        time.sleep(3)
    
    def test_falta_da_senha_CT02(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        retorno_de_erro = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        self.assertEqual('Epic sadface: Password is required', retorno_de_erro)
        time.sleep(3)
    
    def test_falta_do_username_CT03(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        retorno_de_erro = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        self.assertEqual('Epic sadface: Username is required', retorno_de_erro)
        time.sleep(3)
    
    def test_username_travado_CT04(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('locked_out_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        retorno_de_erro = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        self.assertEqual('Epic sadface: Sorry, this user has been locked out.', retorno_de_erro)
        time.sleep(3)
        
    def test_username_incorreto_CT05(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('test1')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        retorno_de_erro = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        self.assertEqual('Epic sadface: Username and password do not match any user in this service', retorno_de_erro)
        time.sleep(3)
    
    def test_senha_incorreta_CT06(self):
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('testesenha')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        time.sleep(2)
        botao_login.click()
        time.sleep(2)
        retorno_de_erro = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        self.assertEqual('Epic sadface: Username and password do not match any user in this service', retorno_de_erro)
        time.sleep(3)
    
if __name__ == '__main__':
        unittest.main()      

