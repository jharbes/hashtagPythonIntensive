from playwright.sync_api import sync_playwright
import time
import pyautogui # importado apenas para testes

# subprocess.run(["playwright", "install", "chromium"])  # ???

# baixar os navegadores do playwright:
# comando: python -m playwright install

# por default o playwright cria o navegador em 'headless'
with sync_playwright() as p:
    navegador=p.chromium.launch(headless=False) # chrome, opera
    # navegador=p.firefox # firefox
    # navegador=p.webkit # safari

    pagina=navegador.new_page()
    pagina.goto('https://github.com/jharbes')

    # pagina.locator('xpath=/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]').click() # clica no elemento com base em seu xpath

    pagina.fill('xpath=/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]','Python Playwright')

    time.sleep(3)


