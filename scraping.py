import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ChromeDriver:
    driver = webdriver.Chrome()
    driver.get('https://juizdefora.branetlogistica.com.br/doms')

    def logaSistema(self, userin, passwordin):
        user = self.driver.find_element(By.ID, "j_idt19:login")
        password = self.driver.find_element(By.ID, "j_idt19:senha") 
        user.send_keys(userin)
        password.send_keys(passwordin)
        btlogin = self.driver.find_element(By.NAME, "j_idt19:j_idt25")
        btlogin.click()
        self.driver.refresh()
        
    
    def puxaItens(self, page):

        lista = []

        self.driver.get(page)
        self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='pesquisa']/fieldset/legend").click()
        time.sleep(1)
        input("next step [Y/N]?")
        self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form/fieldset/div/button/span").click()
        time.sleep(3) 

        select = Select(self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div[1]/select"))
        select.select_by_value('500')
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div/table/thead/tr/th[2]").click()
        time.sleep(3)
        navigator = self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div[1]/span[2]")
        navigator = navigator.find_elements(By.TAG_NAME, 'a')
        
        for i in range(len(navigator)):
            if i != 0:
                navigator[i].click();
                time.sleep(3)
                
            rows= self.driver.find_elements(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div/table/tbody/tr")
            for row in rows:
                cels = row.find_elements(By.TAG_NAME, 'td')
                lista.append([cels[1].text, cels[2].text, cels[5].text])

            navigator = self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div[1]/span[2]")
            navigator = navigator.find_elements(By.TAG_NAME, 'a')

        return lista

    def quitDriver(self):
        self.driver.quit()
