# Recomendacao do selenium utilizar os navegadores Firefox ou Google Chrome

# webdriver
# firefox -> geckodriver
# chrome -> chromedriver

from selenium import webdriver # importa o modulo de utilizacao do browser do selenium
import time


# Passo a passo

## Passo 1: Abrir o navegador

navegador=webdriver.Chrome()
navegador.get('https://www.google.com/')

time.sleep(1)
# navegador=webdriver.Firefox()


# Passo 2: Importar a base de dados

import pandas as pd

tabela=pd.read_excel('C:\\Users\\jharbes\\Documents\\GitHub\\hashtagPython\\aula03-automacaoWeb\\commodities.xlsx')
print(tabela)


for linha in tabela.index:
    produto=tabela.loc[linha,'Produto']
    print(produto)
    produto=produto.replace('ó','o').replace('ã','a').replace('á','a').replace('ç','c').replace('é','e').replace('ú','u').lower() # retirando todos os caracteres especiais para que o link nao quebre na consulta

    link=f'https://www.melhorcambio.com/{produto}-hoje'
    navegador.get(link)

    precoProduto=navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value') # usar copy xpath do site no elemento desejado (CTRL+SHIFT+C -> CLICAR NO ELEMENTO DESEJADO -> CLICAR SEGUNDO BOTAO MOUSE -> COPY XPATH)
    print(precoProduto) 

"""
Elemento em questão abaixo:

<input type="text" value="85,49" class="text-verde" id="comercial" calc="sim">
"""

# Opções para serem feitas com os elementos:

# .click() -> clicar
# .send_keys('texto') -> escrever
# .get_attribute() - > pegar um valor

# Passo 3: Para cada produto da base de dados
# Passo 4: Pesquisar o preco do produto
# Passo 5: atualizar o preço na base de dados
# Passo 6: Decidir quais produtos comprar