from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://www.saucedemo.com/")  # Site de teste

    # Faz login
    pagina.fill("input[name='user-name']", "standard_user")
    pagina.fill("input[name='password']", "secret_sauce")
    pagina.click("input[type='submit']")

    # Esperar a página carregar completamente
    pagina.wait_for_selector(".inventory_item")

    # Extrair nome, preço e imagem dos produtos
    produtos = []
    itens = pagina.locator(".inventory_item").all()  # Pega todos os produtos

    for item in itens:
        nome = item.locator(".inventory_item_name").inner_text()
        preco = item.locator(".inventory_item_price").inner_text()
        imagem = item.locator(".inventory_item_img img").get_attribute("src")  # Pega o link da imagem
        
        produtos.append({"Nome": nome, "Preço": preco, "Imagem": f"https://www.saucedemo.com/{imagem}"})

    navegador.close()

# Criar DataFrame e salvar no Excel
df = pd.DataFrame(produtos)
df.to_excel("produtos_saucedemo.xlsx", index=False)

print("Arquivo Excel salvo com sucesso!")
