# Utilizando biblioteca de automacao pyautogui

import pyautogui
import time # para usar o time.sleep()

pyautogui.click # clique com o mouse
# pyautogui.click(x,y) - local da tela
# pyautogui.click(x,y, button='right') - botao direito do mouse
# pyautogui.click(x,y , clicks=2) - duplo clique do botao do mouse
#  
pyautogui.write # escrever um texto

pyautogui.press # apertar uma tecla

pyautogui.hotkey # apertar uma combinacao de teclas, ex: CTRL+D

pyautogui.PAUSE # pause que funcionará entre TODOS os comandos do pyautogui valor em segundos

# Passo a passo

# setar Pausa:
pyautogui.PAUSE = 2

# Passo 1: Entrar no sistema da empresa (no link)

## Com o navegador fechado:
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5) # faz esperar cinco segundos antes do proximo comando
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter')

## Com o navegador aberto:
# pyautogui.hotkey('ctrl', 't')
# pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
# pyautogui.press('enter')



# Passo 2: Fazer login

## Clicar no espaço de login e escrever o login

# utilizaremos os procedimentos abaixo para descobrir qual a posicao do mouse na tela na aba de navegacao ou qualquer outra tela desejada, o time sera o tempo habil de posicionar onde quer o mouse, depois ele ira printar o ponto exato desejado
# time.sleep(5)
# print(pyautogui.position())

time.sleep(3)

## Preenchendo o login (com clique de mouse ou tab)

pyautogui.press('tab')
# pyautogui.click(x=700, y=371) # vamos tentar com sequencias de tab em vez de cliques com mouse
pyautogui.write('meu_login')

## Preenchendo a senha (com clique de mouse ou tab)

pyautogui.press('tab')
# pyautogui.click(x=762, y=446)
pyautogui.write('minha_senha')

## Dando enter e entrando no sistema

pyautogui.press('tab')
# pyautogui.click(x=775, y=519)
pyautogui.press('enter')

time.sleep(5)

## Exportar a base de dados

# pyautogui.click(x=819, y=540, button='right')
# pyautogui.click(x=1063, y=821)
pyautogui.press('tab')
# pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('space')
pyautogui.press('up')                   
pyautogui.press('enter')

time.sleep(3)

pyautogui.press('enter') # faz o download

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

Total Gasto: R${totalGasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${precoMedio:,.2f}

Para qualquer dúvida, estou a disposição.

Atenciosamente,

Jorge Harbes
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')


# Enviar
pyautogui.hotkey('ctrl','enter')



print('Fim da execução')