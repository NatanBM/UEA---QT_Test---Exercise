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
    
    def test_compra_efetuada_com_sucesso_CT01(self):
        botao_insert_item = self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        time.sleep(2)
        botao_cart = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)
        botao_checkout = self.browser.find_element(By.ID,'checkout').click()
        time.sleep(2)
        firstName = self.browser.find_element(By.ID,'first-name')
        firstName.send_keys('Wael')
        lastName = self.browser.find_element(By.ID,'last-name')
        lastName.send_keys('Louzi')
        zipCode = self.browser.find_element(By.ID,'postal-code')
        zipCode.send_keys('23950140')
        time.sleep(2)
        botao_continue = self.browser.find_element(By.ID,'continue').click()
        time.sleep(2)
        botao_finish = self.browser.find_element(By.ID,'finish').click()
        time.sleep(2)
        validacaoComplete = self.browser.find_element(By.CLASS_NAME, 'complete-header').text
        self.assertEqual('Thank you for your order!', validacaoComplete)
        time.sleep(3)
    
    def test_finalizar_compra_com_carrinho_vazio_CT02(self):
        time.sleep(2)
        botao_cart = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)
        validacao_carrinhovazio = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_link').text
        self.assertEqual('', validacao_carrinhovazio)
        botao_checkout = self.browser.find_element(By.ID,'checkout').click()
        time.sleep(2)
        validacao_checkout = self.browser.find_element(By.CLASS_NAME, 'title').text
        self.assertEqual('Your Cart', validacao_checkout) 
        time.sleep(3)     
    
    def test_inserir_item_no_carrinho_fazer_logoff_e_verificar_CT03(self):
        botao_insert_item = self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        time.sleep(2)
        button_cart = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)
        menu = self.browser.find_element(By.CLASS_NAME,'bm-burger-button')
        menu.click()
        time.sleep(2)
        logoff = self.browser.find_element(By.ID, 'logout_sidebar_link')
        logoff.click()
        time.sleep(2)        
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        botao_login.click()
        time.sleep(2) 
        button_cart = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)          
        validacaoinsertedItem = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_link').text
        self.assertEqual('1', validacaoinsertedItem)    
        time.sleep(3)
    
    def test_remover_item_do_carrinho_fazer_logoff_e_verificar_CT04(self):
        button_insert = self.browser.find_element(By.ID,'remove-sauce-labs-bolt-t-shirt')
        button_insert.click()
        time.sleep(2)        
        menu = self.browser.find_element(By.ID,'react-burger-menu-btn').click()
        time.sleep(2)
        logoff = self.browser.find_element(By.ID, 'logout_sidebar_link').click()
        time.sleep(2)        
        campo_login = self.browser.find_element(By.ID,'user-name')
        campo_login.send_keys('standard_user')
        campo_password = self.browser.find_element(By.ID, 'password')
        campo_password.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        botao_login.click()
        time.sleep(2)         
        button_cart = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)          
        validacaoinsertedItem = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_link').text
        self.assertEqual('', validacaoinsertedItem)   
        time.sleep(3)   
    
    def test_falta_do_firstname_CT05(self):
        click_no_carrinho = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)
        botao_checkout = self.browser.find_element(By.ID,'checkout').click()
        time.sleep(2)
        campo_first_name = self.browser.find_element(By.ID,'first-name')
        campo_first_name.send_keys('')
        campo_lastname = self.browser.find_element(By.ID, 'last-name')
        campo_lastname.send_keys('Louzi')
        campo_postalcode = self.browser.find_element(By.ID, 'postal-code')
        campo_postalcode.send_keys('13025-117')
        botao_continue = self.browser.find_element(By.ID, 'continue')
        botao_continue.click()
        time.sleep(2)
        verificacaoDoFirstName = self.browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3').text
        self.assertEqual('Error: First Name is required', verificacaoDoFirstName)
        time.sleep(3)
    
    def test_falta_do_lastname_CT06(self):
        click_no_carrinho = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)
        button_checkout = self.browser.find_element(By.ID,'checkout').click()
        time.sleep(2)
        campo_first_name = self.browser.find_element(By.ID,'first-name')
        campo_first_name.send_keys('Luiz')
        campo_lastname = self.browser.find_element(By.ID, 'last-name')
        campo_lastname.send_keys('')
        campo_postalcode = self.browser.find_element(By.ID, 'postal-code')
        campo_postalcode.send_keys('13025-117')
        botao_continue = self.browser.find_element(By.ID, 'continue')
        botao_continue.click()
        time.sleep(2)
        verificacaodolastname = self.browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3').text
        self.assertEqual('Error: Last Name is required', verificacaodolastname)
        time.sleep(3)
    
    def test_falta_do_CEP_CT07(self):
        click_no_carrinho = self.browser.find_element(By.ID, 'shopping_cart_container').click()
        time.sleep(2)
        button_checkout = self.browser.find_element(By.ID,'checkout').click()
        time.sleep(2)
        campo_first_name = self.browser.find_element(By.ID,'first-name')
        campo_first_name.send_keys('Luiz')
        campo_lastname = self.browser.find_element(By.ID, 'last-name')
        campo_lastname.send_keys('Honório')
        campo_postalcode = self.browser.find_element(By.ID, 'postal-code')
        campo_postalcode.send_keys('')
        botao_continue = self.browser.find_element(By.ID, 'continue')
        botao_continue.click()
        time.sleep(2)
        verificacaodoCEP = self.browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3').text
        self.assertEqual('Error: Postal Code is required', verificacaodoCEP)
        time.sleep(3)  
    
if __name__ == '__main__':
        unittest.main()      

