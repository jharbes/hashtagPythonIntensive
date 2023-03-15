# Análise de Dados com Python

### Desafio:

"""
Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.

Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.

Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.

Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.

Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=share_link
"""

# Passo a passo

# Passo 1: Importar a base de dados

import pandas as pd

tabela=pd.read_csv('C:\\Users\\jharbes\\Documents\\GitHub\\hashtagPython\\aula02-analiseDeDados\\clientes.csv', encoding='latin', sep=';')
# deletar a coluna inutil (informacao que nao te ajuda, te atrapalha)
tabela=tabela.drop('Unnamed: 8',axis=1) # axis(eixo = 0 se for linha e 1 se for coluna), pode ser passado uma lista de colunas/linhas para que todas sejam deletadas no mesmo comando, elas devem estar em formato de lista

# Passo 2: Visualizar a base de dados
    # Entender as informações que você tem disponível
    # Procurar cagadas na base de dados

print(tabela)



# Passo 3: Tratamento dos dados
print(tabela.info()) # imprime as informacoes de cada coluna como numero de valores nao nulos e tipagem de cada uma da colunas

    # 1- deletar as colunas inuteis
    # 2- acertar informacoes que estao sendo reconhecidas de forma errada
    # 3- corrigir informacoes vazias




# Passo 4: Análise Inicial -> Entender a nota dos clientes





# Passo 5: Análise Completa -> Entender como cada característica do cliente impacta na nota

