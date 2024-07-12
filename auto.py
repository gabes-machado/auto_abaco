import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

XPATHS = {
    # XPaths
    'barra_de_pesquisa': '/html/body/div[1]/div/section/div/div/form/div/input',
    'cidade': '/html/body/div[1]/div/section/div/div/div/div/ul/div[1]/li/button',
    'item': '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div',
    'botao_acad': '/html/body/div[1]/main/div[3]/div[2]/div[3]/div[2]/div/a',
    'botao_contato': '/html/body/section[1]/div[1]/section[7]/div/div/div/div/button/svg',
    'contato': '/html/body/section[1]/div[1]/section[7]/div/div/div/div/div/div[1]/a/p'
}

class Scraper:
    def __init__(self):
        self.cidade = input('Insira a cidade: ') # input the user name
        self.driver = self._setup_driver()
    
    def _setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('lang=en')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--incognito')
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
        return driver
    
    def _scrapping(self):
        try:
            self.driver.get('https://totalpass.com/br/mapa/')  # Your initial login URL here
            time.sleep(10)
            self._wait_for_element(XPATHS['barra_de_pesquisa']).click()
            self._wait_for_element(XPATHS['barra_de_pesquisa']).send_keys(self.cidade)
            self._wait_for_element(XPATHS['cidade']).click()
            time.sleep(10)
            self._wait_for_element(XPATHS['item']).click()
            time.sleep(10)
            self._wait_for_element(XPATHS['botao_acad']).click()
            time.sleep(20)
            self._wait_for_element(XPATHS['botao_contato']).click()
            telefone = self._wait_for_element(XPATHS['contato']).text
            return telefone            

        except Exception as e:
            print(f"Error during login: {e}")
