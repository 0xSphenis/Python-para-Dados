# Exercício 09 -  JSON com clientes premium
import json

def processar_clientes_premium(arquivo_origem: str = "clientes_sj90.json",
                               arquivo_destino: str = "clientes_premium.json", limite_saldo: float = 1000.0) -> None:

    print("INICIANDO MOTOR DE SEGMENTAÇÃO...")
    try:
        with open(arquivo_origem, "r", encoding="utf-8") as f_origem:
            clientes = json.load(f_origem)
    except FileNotFoundError:
        print(f"ERRO CRÍTICO: O arquivo '{arquivo_origem}' não foi encontrado.")
        print("Certifique-se de ter executado a exportação da base principal primeiro.")
        return

    clientes_premium = {
        nome: dados
        for nome, dados in clientes.items()
        if dados["saldo"] > limite_saldo
    }

    with open(arquivo_destino, "w", encoding="utf-8") as f_destino:
        json.dump(clientes_premium, f_destino, indent=4, ensure_ascii=False)
    total_exportados = len(clientes_premium)

    print("\nRELATÓRIO DE SEGMENTAÇÃO VIP (MARKETING)")
    print(f"Critério de corte estabelecido : Saldo > R$ {limite_saldo:.2f}")
    print(f"Total de clientes premium      : {total_exportados}")
    print(f"Arquivo de destino gerado      : '{arquivo_destino}'")

processar_clientes_premium()