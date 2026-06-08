# Exercício 08 - exportar clientes em JSON
import json

def exportar_clientes_json(clientes_dict: dict[str, dict], nome_arquivo: str = "clientes_sj90.json") -> None:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(clientes_dict, arquivo, indent=4, ensure_ascii=False)

    print(f"SUCESSO: Base de clientes exportada com segurança para '{nome_arquivo}'.\n")
    print("SIMULANDO SISTEMA DO PARCEIRO (Leitura do JSON):")

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados_importados = json.load(arquivo)

    conteudo_formatado = json.dumps(dados_importados, indent=4, ensure_ascii=False)
    print(conteudo_formatado)

clientes = {
    "Ana Costa": {"cidade": "RJ", "saldo": 1250.75},
    "Bruno Lima": {"cidade": "SP", "saldo": 980.40}
}

exportar_clientes_json(clientes)