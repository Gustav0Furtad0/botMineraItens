import json
import scraping
import tableform

with open("key.json") as file:
    key = json.load(file)

driver = scraping.ChromeDriver;
driver.logaSistema(driver, key['user'], key['password'])
yes = 'Y'
arquivo = tableform.ExTable
while yes == 'Y':

    lista = driver.puxaItens(driver, "https://juizdefora.branetlogistica.com.br/doms/manutencao/mercadoria.xhtml#b")
    print("Construindo tabela")
    nomeTabela = input("Digite o nome da tabela no arquivo: ")
    arquivo.criarTabela(arquivo, nomeTabela, lista)
    yes = input('Quer fazer maus tabela[Y/N]: ')

arquivo.saveArchive(arquivo, 'itensBranetJF.xlsx')
driver.quitDriver(driver)
