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

print('Fim da execução')