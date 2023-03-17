"""

Projeto Ciência de Dados - Previsão de Preços

- Nosso desafio é conseguir prever o preço de barcos que vamos vender baseado nas características do barco, como: ano, tamanho, tipo de barco, se é novo ou usado, qual material usado, etc.

- Base de Dados: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=share_link

"""

# Passo a Passo de um Projeto de Ciência de Dados

# Passo 1: Entendimento do Desafio

# Passo 2: Entendimento da Área/Empresa
    # Prever o preço de um barco baseado nas caracteristicas dele: ano, material, usado/novo, etc.

# Passo 3: Extração/Obtenção de Dados

import pandas as pd

tabela=pd.read_csv(r'C:\Users\jharbes\Documents\GitHub\hashtagPython\aula04-cienciaDeDados\barcos_ref.csv')
print(tabela)


# Passo 4: Ajuste de Dados (Tratamento/Limpeza)

print(tabela.info())

# Base ja está tratada:
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7649 entries, 0 to 7648
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Preco        7649 non-null   int64
 1   TipoBarco    7649 non-null   int64
 2   TipoVenda    7649 non-null   int64
 3   Ano          7649 non-null   int64
 4   Comprimento  7649 non-null   float64
 5   Largura      7649 non-null   float64
 6   Material     7649 non-null   int64
dtypes: float64(2), int64(5)
memory usage: 418.4 KB
None
"""

# Passo 5: Análise Exploratória

# Correlaçao entre as informacoes da base de dados:

print(tabela.corr()) # correlacao representa uma certa proporcionalidade entre o crescimento de dois itens, nesse caso vamos analisar a variacao do preco em relacao as outras colunas da tabela (valor entre 0 e 1, valores negativos representam crescimento em direcoes opostas entre os valores)


print(tabela.corr()['Preco']) # isolando a tabela preco
print(tabela.corr()[['Preco']]) # melhorando a formatacao da coluna

correlacao=tabela.corr()[['Preco']]

import seaborn as sns
import matplotlib.pyplot as plt

# cria o grafico
sns.heatmap(correlacao, cmap='Blues', annot=True) # cria com o seaborn, usando o color map (cmap) de Blues para ficar com tons de azul

# exibe o grafico
plt.show() # exibe com o matplotlib


# Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
    # dividir a tabela entre  x e y  (sendo normalmente y o objetivo e x o resto da tabela)

y=tabela['Preco'] # dados que queremos prever

# x caracteristicas do barco que iremos usar para prever o preco
x=tabela.drop('Preco', axis=1) # a tabela x seriam todas as tabelas exceto a tabela preco, sendo assim o comando seria apague 'Preco' que eh uma coluna (axis=1), retorna a tabela sem a coluna 'Preco'
# axis = 0 -> Linhas, axis=1 -> colunas

# train test split (divisao em treino e teste)



# Passo 7: Interpretação de Resultados
