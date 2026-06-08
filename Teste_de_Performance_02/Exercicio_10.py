# Exercício 10 - CSV com Pandas
import pandas as pd

conteudo_csv = """id,cliente,valor,tipo
1,Ana Costa,250,credito
2,Ana Costa,-100,debito
3,Bruno Lima,400,credito
4,Bruno Lima,-10,debito"""

with open("transacoes.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_csv)

def analisar_transacoes_pandas(caminho_arquivo: str = "transacoes.csv") -> None:

    print("INICIANDO MOTOR ANALÍTICO DO PANDAS...")

    df = pd.read_csv(caminho_arquivo)
    contagem_tipos = df["tipo"].value_counts()
    saldo_clientes = df.groupby("cliente")["valor"].sum()
    
    print("\nRELATÓRIO DE VOLUMETRIA POR TIPO DE TRANSAÇÃO")
    for tipo, quantidade in contagem_tipos.items():
        print(f"-> {tipo.capitalize()}: {quantidade} operação(ões)")

    print("\nRELATÓRIO DE SALDO FINAL CONSOLIDADO (GROUPBY)")
    for cliente, saldo in saldo_clientes.items():
        print(f"-> Cliente: {cliente.ljust(15)} | Saldo Final: R$ {saldo:.2f}")


analisar_transacoes_pandas()