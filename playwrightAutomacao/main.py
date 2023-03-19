from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador=p.chromium # chrome
    # navegador=p.firefox # firefox
    # navegador=p.webkit # safari