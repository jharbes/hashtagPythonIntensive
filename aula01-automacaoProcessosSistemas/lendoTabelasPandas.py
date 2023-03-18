# Passo 4: Calcular os indicadores

import pandas
import pyautogui
import time

pyautogui.PAUSE = 2

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

print(f'{totalGasto=}')
print(f'{quantidade=}')
print(f'{precoMedio=}')



# Passo 5: Enviando email para o chefe

# Entrar no email: https://mail.google.com/mail/u/0/#inbox
# clicar no botao escrever
# preencher as informacoes do email
# enviar

pyautogui.hotkey('ctrl','t') # abrir nova aba do chrome
pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
pyautogui.press('enter')
time.sleep(5)

# clicar no botao escrever
pyautogui.click(x=135, y=240)

# preencher as informacoes do email
# destinatario
pyautogui.write('jharbes@hotmail.com')
pyautogui.press('tab') # escolher o destinatario

pyautogui.press('tab') # passa para o campo assunto(proximo campo do formulario)

import pyperclip

# para usarmos acentos ou caracteres especiais no pyautogui tera que ser feito por meio do pyperclip, faremos a copia do que for escrito com pyperclip.copy e depois copiaremos no formulario, local pertinente com pyautogui.hotkey('ctrl','v') conforme abaixo
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')

pyautogui.press('tab') # passa para o corpo do email (proimo campo do formulario)

texto=f'''
Prezados,
Segue o relatório de compras

Total Gasto: {totalGasto}
Quantidade de Produtos: {quantidade}
Preço Médio: {precoMedio}

Para qualquer dúvida, estou a disposição.

Atenciosamente,

Jorge Harbes
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')


# Enviar
pyautogui.hotkey('ctrl','enter')