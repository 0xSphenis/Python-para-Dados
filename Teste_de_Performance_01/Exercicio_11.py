import json

def exportar_e_verificar_json(dados_produtos: dict, nome_arquivo: str = "produtos.json") -> None:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados_produtos, arquivo, indent=4, ensure_ascii=False)

    print(f"Dados exportados com sucesso para o arquivo '{nome_arquivo}'!\n")

    print("LENDO O SISTEMA DE INTEGRAÇÃO:")

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados_importados = json.load(arquivo)

    print(f"Conteúdo importado: {dados_importados}\n")

    tipo_do_objeto = type(dados_importados)
    print(f"Tipo de dado retornado pelo json.load: {tipo_do_objeto}")

produtos_ecommerce = {
    "Smartphone": {"preco": 2500, "estoque": 12},
    "Notebook": {"preco": 4800, "estoque": 5},
    "Fone Bluetooth": {"preco": 300, "estoque": 25}
}

exportar_e_verificar_json(produtos_ecommerce)