import json

def consolidar_bases_crm(camp1: list[str], camp2: list[str], camp3: list[str],
                         nome_arquivo: str = "clientes_unicos.json") -> None:
    base_unica = set(camp1) | set(camp2) | set(camp3)
    nomes_ordenados = sorted(list(base_unica))

    dados = {
        "total": len(nomes_ordenados),
        "nomes": nomes_ordenados
    }

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print(f"Arquivo '{nome_arquivo}' gerado com sucesso no disco!\n")
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados_importados = json.load(arquivo)

    print("RELATÓRIO DE CONSOLIDAÇÃO DE CAMPANHAS")
    print(f"Total de clientes únicos na base: {dados_importados['total']}")
    print(f"Lista final consolidada: {dados_importados['nomes']}")

campanha_1 = ["Ana", "Bruno", "Carla"]
campanha_2 = ["Bruno", "Daniel", "Eduardo"]
campanha_3 = ["Ana", "Fernanda", "Gustavo"]

consolidar_bases_crm(campanha_1, campanha_2, campanha_3)