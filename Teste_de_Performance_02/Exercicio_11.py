import pandas as pd
import json

massa_dados = {
    "Ana Costa": {"cidade": "RJ", "saldo": 1250.75},
    "Carlos Eduardo": {"cidade": "MG", "saldo": 2500.50},
    "Fernanda Silva": {"cidade": "SP", "saldo": 3200.00}
}
with open("clientes_premium.json", "w", encoding="utf-8") as f:
    json.dump(massa_dados, f, indent=4, ensure_ascii=False)

def auditar_json_com_pandas(caminho_arquivo: str = "clientes_premium.json") -> None:
    print("INICIANDO AUDITORIA COM PANDAS...")

    df = pd.read_json(caminho_arquivo, orient="index")

    print("\nESTRUTURA DO DATAFRAME:")

    print(f"-> Colunas disponíveis : {list(df.columns)}")

    print("-> Tipos de dados (dtypes):")
    print(df.dtypes)

    df_super_premium = df[df["saldo"] > 2000]

    print("\nCLIENTES COM SALDO SUPERIOR A R$ 2000,00")

    print(df_super_premium)
auditar_json_com_pandas()