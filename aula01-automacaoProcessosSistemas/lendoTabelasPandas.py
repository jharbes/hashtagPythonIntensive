# Passo 4: Calcular os indicadores

import pandas

# raw string
# aqui indicamos no comando que o separador é o ; (ponto e virgula), pois o arquivo está usando caractere diferente do usual que é a , (virgula)
tabela=pandas.read_csv(r'C:\Users\Jorge\Desktop\hashtagPython\aula01-automacaoProcessosSistemas\Compras.csv', sep=';')
print(tabela)

# somatorio da coluna Valor Final da tabela
totalGasto=tabela['ValorFinal'].sum()

# somatorio da coluna Quantidade da tabela
quantidade=tabela['Quantidade'].sum()

# preco medio 
precoMedio=totalGasto/quantidade

print(totalGasto)
print(quantidade)
print(precoMedio)