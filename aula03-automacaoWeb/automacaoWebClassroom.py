# Recomendacao do selenium utilizar os navegadores Firefox ou Google Chrome

# webdriver
# firefox -> geckodriver
# chrome -> chromedriver

from selenium import webdriver
import time

navegador=webdriver.Chrome()

time.sleep(5)
# navegador=webdriver.Firefox()

# Passo a passo

# Passo 1: Abrir o navegador
# Passo 2: Importar a base de dados
# Passo 3: Para cada produto da base de dados
# Passo 4: Pesquisar o preco do produto
# Passo 5: atualizar o preço na base de dados
# Passo 6: Decidir quais produtos comprar